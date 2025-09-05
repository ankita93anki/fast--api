from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    email: str
    age: int

class Product(BaseModel):
    name:str
    price:int
    discount:int 
    discounted_price:float

app = FastAPI()

@app.post('/addproduct')
def addProduct(product:Product):
    product.discounted_price = product.price - (product.price * product.discount)/100
    return product

@app.post('/adduser')
def addUser(profile:Profile):
    return profile

