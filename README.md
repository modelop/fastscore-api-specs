
# fastscore-api-specs

OpenAPI specifications for the following FastScore microservices:

* Connect (connect.yaml)
* Model Manage (model-manage.yaml)
* Engine X (engine-x.yaml)

# How to validate

It is a good habit to validate any updated specification before commiting
changes. Use the online validator as follows:

```
curl -X POST http://online.swagger.io/validator/debug --data-binary @<spec-file.yaml>
```

The validator may return a "malformed or unreadable swagger supplied" message
without any errors or warnings. The message can be disregarded as it shows that
the validator cannnot access the type definition file (types.yaml).

