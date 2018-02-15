
# fastscore-api-specs

OpenAPI specifications for the following FastScore microservices:

* Connect (connect.yaml)
* Model Manage (model-manage.yaml)
* Engine (engine.yaml)

TODO: create a script to extract connect.yaml, model-manage.yaml, and
engine.yaml from suite-proxy.yaml.

# How to validate

Run 'make validate' before committing changes.

# How to split API

Sometimes it is more convenient to have a separate Swagger spec for each of the
service type. Use split_spec.py to create/update these specs.
```
python split_spec.py suite-proxy-v1.yaml
```

