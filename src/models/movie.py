from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .associations import movies_actors
from .base import Base

class Movie(Base):
    __tablename__ = 'movies'

    ID = Column(Integer, primary_key=True, index=True)
    Title = Column(String(100))
    ReleaseYear = Column(Integer)
    Genre = Column(String(50))
    Director = Column(String(100))

    actors = relationship("Actor", secondary=movies_actors, back_populates="movies")

