from pydantic import BaseModel
from typing import List
from .actor import Actor  # Import Actor schema for nested relationship

class MovieBase(BaseModel):
    """
    Base schema for Movie. Contains common attributes for Movie.
    """
    Title: str  # Movie title
    ReleaseYear: int  # Year of release
    Genre: str  # Genre of the movie
    Director: str  # Director of the movie

class MovieCreate(MovieBase):
    """
    Schema for creating a Movie.
    Used when receiving data from the client to create a new Movie.
    """
    pass  # No additional fields are required for creation

class MovieUpdate(MovieBase):
    """
    Schema for updating a Movie.
    Used when receiving data from the client to update an existing Movie.
    """
    pass  # No additional fields are required for updating

class Movie(MovieBase):
    """
    Full Movie schema, including Movie ID and related Actors.
    Used for returning Movie data.
    """
    ID: int  # Movie's unique identifier
    actors: List[Actor] = []  # List of actors associated with the movie

    class Config:
        """ Pydantic configuration for ORM compatibility """
        orm_mode = True
