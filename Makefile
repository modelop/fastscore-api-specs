
.PHONY: default

validate:
	swagger validate connect.yaml
	swagger validate model-manage.yaml
	swagger validate engine-x.yaml

