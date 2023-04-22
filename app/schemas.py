from pydantic import BaseModel
import datetime

class EventCreate(BaseModel):
    type:str
    detail:str
    player_id:int

class EventDb(EventCreate):
    id:int
    timestamp:str = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    
    class Config:
        orm_mode = True

class PlayerCreate(BaseModel):
    name:str

class PlayerBase(PlayerCreate):
    id:int

    class Config:
        orm_mode = True
    
class PlayerDb(PlayerBase):
    events:list

    class Config:
        orm_mode = True