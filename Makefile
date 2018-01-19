
.PHONY: validate

SWAGGER := Engine.swagger.json \
           ModelManage.swagger.json \
           Connect.swagger.json

validate:
	swagger validate suite-proxy-v1.yaml
	swagger validate suite-proxy-v2.yaml

s3-sync:
	./split_spec.py suite-proxy-v1.yaml
	aws s3 cp --acl public-read Connect.swagger.json s3://fastscore-api-swagger
	aws s3 cp --acl public-read ModelManage.swagger.json s3://fastscore-api-swagger
	aws s3 cp --acl public-read Engine.swagger.json s3://fastscore-api-swagger
	aws s3 cp --acl public-read types-v1.yaml s3://fastscore-api-swagger

