from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)

    events = relationship("Event",back_populates="owner")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer,primary_key=True)
    type = Column(String)
    detail = Column(String)
    timestamp = Column(String)
    player_id = Column(Integer,ForeignKey("players.id"))

    owner =relationship("Player",back_populates="events")

