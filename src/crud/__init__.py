"""
Initialization file for the CRUD package.
This allows importing CRUD functions from a single module.
"""

from .movie import get_movies, get_movie, create_movie, delete_movie
from .actor import get_actors, get_actor, create_actor, delete_actor
