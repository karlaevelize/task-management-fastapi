from typing import Union

from pydantic import BaseModel

# item stuff
class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# list stuff
class ListBase(BaseModel):
    name: str

class ListCreate(ListBase):
    pass

class List(ListBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
