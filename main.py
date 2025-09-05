from fastapi import FastAPI

app = FastAPI()

@app.get('/user/admin')
def admin():
    return {'This is admin page'}

#path parameter
@app.get('/user/{username}')
def profile(username):
    return {f'This is a profile page for {username}'}

#required query parameter
@app.get('/products')
def products(id:int=None,price:int=None):
    return {f'Product with an id: {id} and price = {price}'}

#use path & query parametr
@app.get('/profile/{userid}/comments')
def profile(userid:int,commentId:int):
    return {f'Profile page for user with userid {userid} and comment for comment id {commentId}'}

