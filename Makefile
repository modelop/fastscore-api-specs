
.PHONY: validate

SWAGGER := Engine.swagger.json \
           ModelManage.swagger.json \
           Connect.swagger.json

validate:
	swagger validate suite-proxy-v1.yaml
	swagger validate suite-proxy-v2.yaml

split:
	./split_spec.py suite-proxy-v1.yaml
