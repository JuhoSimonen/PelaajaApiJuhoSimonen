from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/players/",response_model=schemas.PlayerBase)
def create_player(player:schemas.PlayerCreate,db:Session=Depends(get_db)):
    return crud.create_player(db=db,player=player)

@app.get("/players/", response_model=list[schemas.PlayerDb])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = crud.get_players(db, skip=skip, limit=limit)
    return players