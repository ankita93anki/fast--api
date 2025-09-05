from fastapi import FastAPI

app = FastAPI()

@app.get('/user/admin')
def admin():
    return {'This is admin page'}

@app.get('/user/{username}')
def profile(username):
    return {f'This is a profile page for {username}'}


