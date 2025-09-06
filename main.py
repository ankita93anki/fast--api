from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl
from typing import Set,List

class Profile(BaseModel):
    name: str
    email: str
    age: int

class Image(BaseModel):
    url:HttpUrl
    name:str

class Product(BaseModel):
    name:str
    price:int = Field(title="Price of the item", description="This would be the price of the item being added", gt=0)
    discount:int 
    discounted_price:float
    tags: Set[str] = []
    image:List[Image]

class Offer(BaseModel):
    name:str
    description:str
    price:float
    products:List[Product]

class User(BaseModel):
    name:str
    email:str

app = FastAPI()

@app.post('/addoffer')
def addoffer(offer:Offer):
    return {offer}

@app.post('/purchase')
def purchase(user:User, product:Product):
    return {'user':user,"product":product}

@app.post('/addproduct/{product_id}')
def addProduct(product:Product, product_id: int, category:str):
    product.discounted_price = product.price - (product.price * product.discount)/100
    return {"product_id":product_id,"product":product, "category":category}

@app.post('/adduser')
def addUser(profile:Profile):
    return profile

