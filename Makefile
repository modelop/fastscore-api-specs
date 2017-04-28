
.PHONY: default

validate:
	swagger validate suite-proxy.yaml
	swagger validate login.yaml

