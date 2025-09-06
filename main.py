from fastapi import FastAPI, Form
from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from typing import Set,List
from datetime import date, datetime, time, timedelta
from uuid import UUID

class Event(BaseModel):
    event_id: UUID
    start_date: date
    start_time: datetime
    end_Time: datetime
    repeat_time: time
    execute_after: timedelta

class Profile(BaseModel):
    name: str = Field(example="abc")
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

    model_config = ConfigDict(json_schema_extra={
        "example":{
            "name":"Phone",
            "price":100,
            "discount":10,
            "discounted_price":0,
            "tags":["Electronics","Computers"],
             "image":[
                    {
                        "url":"http://www.google.com",
                        "name": "phone image"
                    },
                    {
                        "url":"http://www.google.com",
                        "name": "phone image side view"
                    }
            ]
        }
    })
   
class Offer(BaseModel):
    name:str
    description:str
    price:float
    products:List[Product]

class User(BaseModel):
    name:str
    email:str

app = FastAPI()

@app.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    #pip install python-multipart
    return {"username":username}

@app.post('/addEvent')
def addevent(event: Event):
    return event

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

