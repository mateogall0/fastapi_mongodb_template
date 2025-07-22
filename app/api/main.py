from fastapi import FastAPI
from app.utils import DEBUG
from app.api import init_api, lifespan


# fastapi instance
app = FastAPI(debug=DEBUG,
              title='API',
              description='Fastapi and MongoDB app',
              lifespan=lifespan)

init_api(app)
