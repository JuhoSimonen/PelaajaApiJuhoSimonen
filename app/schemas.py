from pydantic import BaseModel

class EventBase(BaseModel):
    type:str
    detail:str

class EventDb(EventBase):
    id:int
    timestamp:str
    player_id:int

    class Config:
        orm_mode = True

class PlayerCreate(BaseModel):
    name:str

class PlayerBase(PlayerCreate):
    id:int
    
class PlayerDb(PlayerBase):
    events:list(EventDb) = []

    class Config:
        orm_mode = True