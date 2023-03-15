from typing import List
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import crud, models, database, schemas

# from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
  CORSMiddleware, 
  allow_origins=origins, 
  allow_credentials=True, 
  allow_methods=["*"],
  allow_headers=["*"]
)

# Dependency
def get_db():
  db = database.SessionLocal()
  try:
    yield db
  finally:
    db.close()

# get list with its items
@app.get("/lists", response_model=List[schemas.List])
def read_lists(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
  lists = crud.get_lists(db, skip=skip, limit=limit)
  if lists is None:
    raise HTTPException(status_code=404, detail="No lists found")
  return lists

# create list
@app.post("/lists", response_model=schemas.List)
def create_list(list: schemas.List, db: Session = Depends(get_db)):
  return crud.create_list(db, list=list)

# delete list
@app.delete("/lists", response_model=str)
def delete_lists(list_id: int, db: Session = Depends(get_db)):
  return crud.delete_list(db, list_id=list_id)
