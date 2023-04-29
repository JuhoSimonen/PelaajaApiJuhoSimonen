from sqlalchemy.orm import Session
from . import models,schemas
import datetime

def get_players(db:Session,skip = 0,limit:int=100):
    return db.query(models.Player).offset(skip).limit(limit).all()

def get_player(db:Session,player_id:int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()

def create_player(nimi:schemas.PlayerCreate,db:Session):
    db_player = models.Player(name = nimi.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player

def create_player_event(db:Session,event:schemas.EventCreate,player_id:int):
    db_event = models.Event(**event.dict(),player_id = player_id,timestamp = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def get_player_events(db:Session,id:int,type:str):
    if type is None:
        return db.query(models.Event).filter(models.Event.player_id == id).all()
    player_db = db.query(models.Event).filter(models.Event.player_id == id,models.Event.type == type).all()
    return player_db
    
def get_events(db:Session,type:str):
    if type is None:
        return db.query(models.Event).all()
    return db.query(models.Event).filter(models.Event.type == type).all()
    


