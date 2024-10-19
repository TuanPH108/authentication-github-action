from fastapi import APIRouter

test_route = APIRouter(prefix='/test')

@test_route.get('/test-deploy')
def test_deploy():
    return {
        'Hello' : 'World'
    }