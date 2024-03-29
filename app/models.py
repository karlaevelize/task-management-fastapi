from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class List(Base):
    __tablename__ = "lists"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    color = Column(String, default="black")
    order = Column(Integer, unique=True, index=True)

    items = relationship("Item", back_populates="list")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    list_id = Column(Integer, ForeignKey("lists.id"))

    list = relationship("List", back_populates="items")
    