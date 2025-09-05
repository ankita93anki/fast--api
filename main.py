from fastapi import FastAPI

app = FastAPI()

@app.get('/user/admin')
def admin():
    return {'This is admin page'}

#path parameter
@app.get('/user/{username}')
def profile(username):
    return {f'This is a profile page for {username}'}

#query parameter
@app.get('/products')
def products(id:int=1,price:int=2):
    return {f'Product with an id: {id} and price = {price}'}


