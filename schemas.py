from pydantic import BaseModel
from typing import Tuple

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True

class Attractions(BaseModel):
    id: int
    name: str
    type: str
    region: str
    locality: str
    geolocation: str

    class Config:
        orm_mode = True

class AttractionsType(BaseModel):
    type: str
    class Config:
        orm_mode = True