# FastAPI and MongoDB template

## Env
```bash
# prod, dev, test
ENV=

# optional, otherwise state each value
MONGO_URI=
MONGO_URI_DEV=
MONGO_URI_TEST=

MONGO_USER=
MONGO_PASSWORD=
MONGO_HOST=
MONGO_PORT=

DATABASE_NAME=
DATABASE_NAME_DEV=
DATABASE_NAME_TEST=

# default: '?authSource=admin'
# can be replaced by an empty string (e.g "")
DATABASE_ARGS=

# obtain gateway access token
BITA_SDK_INITIAL_ACCESS_TOKEN=
BITA_GATEWAY_HOST=

SECRET_KEY_JWT=
```

## Run
```bash
uvicorn app.main:app
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
