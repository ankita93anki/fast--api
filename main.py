from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    email: str
    age: int

app = FastAPI()

@app.post('/adduser')
def addUser(profile:Profile):
    return profile