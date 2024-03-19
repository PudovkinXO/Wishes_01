from fastapi import FastAPI
from pydantic import BaseModel, Field

from typing import List

app = FastAPI(
    title = "MyWishes"
)
wishes = []

@app.get("/")
def hi():
    return 'Hi!'



class Wish(BaseModel):
    id: int
    wish_name: str
    description: str
    price: float = Field(ge = 0)
    tags: list = []


@app.post("/add_wish")
def make_new_wish(new_wishes: List[Wish]):
    wishes.extend(new_wishes)
    return {"created": True}  

@app.get("/all_wishes")
def get_all_wishes():
    return {
        "wish": wishes}

