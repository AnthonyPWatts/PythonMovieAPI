from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .associations import movies_actors
from .base import Base

class Actor(Base):
    __tablename__ = 'actors'

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String(100))
    BirthDate = Column(String)

    movies = relationship("Movie", secondary=movies_actors, back_populates="actors")
