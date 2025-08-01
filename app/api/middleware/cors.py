from fastapi.middleware.cors import CORSMiddleware
from app.infra.security.origins import read_origins


args = {
    'middleware_class': CORSMiddleware,
    'allow_origins': read_origins(),
    'allow_credentials': True,
    'allow_methods': ['*'],
    'allow_headers': ['*']
}
