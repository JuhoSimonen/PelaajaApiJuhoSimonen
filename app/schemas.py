from pydantic import BaseModel


class EventType(BaseModel):
    type:str

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

class PlayerCreate(BaseModel):
    name:str

    class Config:
        orm_mode = True

class PlayerBase(PlayerCreate):
    id:int

    class Config:
        orm_mode = True
    
class PlayerDb(PlayerBase):
    events:list

    class Config:
        orm_mode = True

    