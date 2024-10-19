from fastapi import FastAPI
from .router.test_router import test_route
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

app.include_router(test_route)

@app.get('/')
def index():
    return {
        'index' : 'Hello world'
    }