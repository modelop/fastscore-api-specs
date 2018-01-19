
# fastscore-api-specs

OpenAPI specifications for the following FastScore microservices:

* Connect (connect.yaml)
* Model Manage (model-manage.yaml)
* Engine (engine.yaml)

# How to validate

Run 'make validate' before committing changes.

# How to sync readme.io API reference

Run 'make s3-sync'.

This splits the master (proxy) API spec into 3 separate specifications and
uploads them to S3 bucket.

Go to the readme.io dashboard > Reference Docs and click 'resync' for each API
in the list.

