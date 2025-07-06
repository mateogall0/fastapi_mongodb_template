from fastapi import APIRouter
from app.api.handlers import main


main_router = APIRouter(tags=['Main'])

main_router.get('/', status_code=200)(main.get_main_handler)
