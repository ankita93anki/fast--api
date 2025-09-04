from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'Hello world!'

@app.get('/property')
def property():
    return 'This is a property range'

@app.get('/movies')
def movies():
    return {'movie list': {'Movie 1','Movie 2'}}
