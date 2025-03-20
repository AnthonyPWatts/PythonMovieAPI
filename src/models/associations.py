# Desc: Module for defining association tables for many-to-many relationships
from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

# Association table for many-to-many relationship between movies and actors
movies_actors = Table(
    "MoviesActors",
    Base.metadata,
    Column("MovieID", Integer, ForeignKey("movies.ID"), primary_key=True),
    Column("ActorID", Integer, ForeignKey("actors.ID"), primary_key=True)
)
