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

@app.get("/players/{id}",response_model=schemas.PlayerDb)
def read_player(id:int,db:Session=Depends(get_db)):
    db_player = crud.get_player(db,player_id=id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_player

@app.post("/players/{id}/events",response_model=schemas.EventDb,status_code=201)
def create_event_for_player(
    id:int,event:schemas.EventCreate,db: Session=Depends(get_db)
):
    db_player = crud.get_player(db,player_id=id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="User not found")
    if event.type != "level_started" and event.type != "level_solved":
        raise HTTPException(status_code=400,detail="Unknown event type")
    return crud.create_player_event(db=db,event=event,player_id=id)
'''
@app.get("/events/", response_model=list[schemas.EventDb])
def read_events(event_type:schemas.EventType, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    events = crud.get_events(db, skip=skip, limit=limit,type = event_type.type)
    return events
'''
@app.get("/events/", response_model=list[schemas.EventDb])
def read_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_events = crud.get_events(db, skip=skip, limit=limit)
    return db_events