# FastAPI and MongoDB template

## Structure
```
app
├── api
│   ├── bootstrap
│   ├── dependencies
│   ├── handlers
│   ├── middleware
│   ├── routes
│   │   └── v1
│   └── schemas
├── core
│   └── models
├── infra
│   ├── db
│   ├── external
│   ├── repository
│   ├── security
│   └── utils
└── service
```

## Run
```bash
uvicorn app.api.main:app
```

To get options:
```bash
univcorn --help
```


## Tests
Testing is implemented using the PyTest framework:
```bash
pytest
```

## Run scripts
```bash
python3 -m scripts.<script_name>
```
