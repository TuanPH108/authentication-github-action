from fastapi import FastAPI
from .router.test_router import test_route

app = FastAPI()

app.include_router(test_route)

@app.get('/')
def index():
    return {
        'index' : 'Hello world'
    }