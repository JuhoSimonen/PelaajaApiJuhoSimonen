from pydantic import BaseModel

#Event

class EventType(BaseModel):
    type:str | None = None

    class Config:
        orm_mode = True

class EventCreate(EventType):
    detail:str

    class Config:
        orm_mode = True

class EventDb(EventCreate):
    id:int
    timestamp:str
    player_id:int
    
    class Config:
        orm_mode = True

#Player

class PlayerCreate(BaseModel):
    name:str

    class Config:
        orm_mode = True

class PlayerBase(PlayerCreate):
    id:int

    class Config:
        orm_mode = True
    
class PlayerDb(PlayerBase):
    events:list[EventDb]

    class Config:
        orm_mode = True

    