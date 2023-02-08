from typing import Union
from pydantic import BaseModel

# item stuff
class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    list_id: int

    class Config:
        orm_mode = True

# list stuff
class ListBase(BaseModel):
    name: str
    color: str
    order: int

class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True