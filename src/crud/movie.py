from sqlalchemy.orm import Session
from ..schemas.movie import MovieCreate, MovieUpdate
from ..models import Movie

def get_movies(db: Session):
    """
    Retrieve a list of all movies from the database.
    """
    return db.query(Movie).all()

def get_movie(db: Session, movie_id: int):
    """
    Retrieve a single movie by its ID.
    """
    return db.query(Movie).filter(Movie.ID == movie_id).first()

def create_movie(db: Session, movie: MovieCreate):
    """
    Create a new movie in the database.
    """
    db_movie = Movie(**movie.model_dump())  # Updated for Pydantic v2
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def delete_movie(db: Session, movie_id: int):
    """
    Delete a movie by its ID.
    """
    db_movie = db.query(Movie).filter(Movie.ID == movie_id).first()
    if db_movie:
        db.delete(db_movie)
        db.commit()
    return db_movie

def update_movie(db: Session, movie_id: int, movie: MovieUpdate):
    """
    Update a movie and return the updated movie.
    """
    db_movie = db.query(Movie).filter(Movie.ID == movie_id).first()
    if db_movie:
        db_movie.Title = movie.Title
        db_movie.ReleaseYear = movie.ReleaseYear
        db_movie.Genre = movie.Genre
        db_movie.Director = movie.Director
        db.commit()
        # Refresh to ensure that we have the updated data from the DB
        db.refresh(db_movie)
        return db_movie
    return None
