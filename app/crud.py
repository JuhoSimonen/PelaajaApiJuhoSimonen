from sqlalchemy.orm import Session
from . import models,schemas

def get_players(db:Session,skip = 0,limit:int=100):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player(db:Session,player_id:int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def create_player(db:Session,player:schemas.PlayerCreate):
    db_player = models.Player(name = player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def get_events(db:Session,skip: int = 0,limit:int=100):
    return db.query(models.Event).offset(skip).limit(limit).all()

def create_player_event(db:Session,event:schemas.EventCreate,id:int):
    db_event = models.Event(**event.dict(),player_id = id)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

