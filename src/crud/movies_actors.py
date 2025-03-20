from sqlalchemy.orm import Session
from ..models.associations import movies_actors
from ..models import Movie, Actor

# Add an actor to a movie
def add_actor_to_movie(db: Session, movie_id: int, actor_id: int):
    movie = db.query(Movie).filter(Movie.ID == movie_id).first()
    actor = db.query(Actor).filter(Actor.ID == actor_id).first()
    
    if movie and actor:
        movie.actors.append(actor)  # Add the actor to the movie's actors list
        db.commit()
        db.refresh(movie)
        return movie
    return None

# Remove an actor from a movie
def remove_actor_from_movie(db: Session, movie_id: int, actor_id: int):
    movie = db.query(Movie).filter(Movie.ID == movie_id).first()
    actor = db.query(Actor).filter(Actor.ID == actor_id).first()
    
    if movie and actor:
        movie.actors.remove(actor)  # Remove the actor from the movie's actors list
        db.commit()
        db.refresh(movie)
        return movie
    return None

# Get all actors for a movie
def get_actors_for_movie(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.ID == movie_id).first()
    if movie:
        return movie.actors
    return None

# Get all movies for an actor
def get_movies_for_actor(db: Session, actor_id: int):
    actor = db.query(Actor).filter(Actor.ID == actor_id).first()
    if actor:
        return actor.movies
    return None