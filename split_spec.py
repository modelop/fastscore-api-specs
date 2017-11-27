#!/usr/bin/env python2

import sys
import yaml, json
import copy

KNOWN_TAGS = [
    "Connect",
    "ModelManage",
    "Engine"
]

def main():
    if len(sys.argv) != 2:
        print "Usage: split_spec.py <suite-spec-file.yaml>"
        sys.exit(1)

    suite_spec_file = sys.argv[1]
    suite_spec = yaml.load(open(suite_spec_file))

    for tag in KNOWN_TAGS:
        spec = copy.deepcopy(suite_spec)
        filter_spec(spec, tag)
        explode_refs(spec)
        spec_file = "{}.swagger.json".format(tag)
        with open(spec_file, "w") as f:
            json.dump(spec, f, indent=2)
            print "{} written".format(spec_file)

def filter_spec(spec, tag):
    spec['info']['title'] = "FastScore {} API".format(tag)
    paths = spec['paths']
    for path in paths.keys():
        ops = paths[path]
        for op in ops.keys():
            if not tag in ops[op]['tags']:
                del ops[op]
        if len(ops) == 0:
            del paths[path]
        else:
            instance_ref = { '$ref': '#/parameters/instance' }
            for op in ops.keys():
                del ops[op]['tags']
                ops[op]['parameters'].remove(instance_ref)
    spec['paths'] = {chop_path(path): ops for path,ops in paths.items()}

def explode_refs(spec):
    if isinstance(spec, dict):
        for prop in spec:
            if isinstance(spec[prop], dict) and \
               '$ref' in spec[prop] and \
               not spec[prop]['$ref'].startswith('#'):
                (filename,objname) = spec[prop]['$ref'].split("#/")
                target = yaml.load(open(filename))
                spec[prop] = target[objname]
            else:
                explode_refs(spec[prop])
    elif isinstance(spec, list):
        for item in spec:
            explode_refs(item)

def chop_path(path):
    prefix = '/{instance}'
    if path.startswith(prefix):
        return path[len(prefix):]
    else:
        return path

if __name__ == "__main__":
    main()

