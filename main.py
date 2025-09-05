from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'Hello world!'

#id here is a path parameter
@app.get('/property/{id}')
def property(id:int):
    return {f'This is a property range for property {id}'}

@app.get('/profile/{username}')
def profile(username: str):
    return {f'This is profile page for user : {username}'}

@app.get('/movies')
def movies():
    return {'movie list': {'Movie 1','Movie 2'}}
