from pydantic import BaseModel

#Event

class EventCreate(BaseModel):
    type:str
    detail:str
    class Config:
        orm_mode = True

class EventBase(BaseModel):
    id:int
    type:str | None = None
    detail:str

    class Config:
        orm_mode = True

class EventDb(EventBase):
    
    timestamp:str
    player_id:int
    
    class Config:
        orm_mode = True

#Player

class PlayerCreate(BaseModel):
    name:str

class PlayerBase(BaseModel):
    id:int
    name:str
    class Config:
        orm_mode = True
    
class PlayerDb(PlayerBase):
    events:list[EventDb]

    class Config:
        orm_mode = True

    