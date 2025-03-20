from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.movie import MovieCreate, MovieUpdate
from ..crud import movie as movie_crud
import logging

logger = logging.getLogger()
router = APIRouter()

@router.get("/")
def read_movies(db: Session = Depends(get_db)):
    logger.info("Fetching all movies")
    return movie_crud.get_movies(db)

@router.get("/{movie_id}")
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    logger.info("Fetching movie with ID: %d", movie_id)
    movie = movie_crud.get_movie(db, movie_id)
    if movie is None:
        logger.error("Movie with ID %d not found", movie_id)
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    logger.info("Creating a new movie with title: %s", movie.title)
    return movie_crud.create_movie(db, movie)

@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    logger.info("Deleting movie with ID: %d", movie_id)
    movie = movie_crud.delete_movie(db, movie_id)
    if movie is None:
        logger.error("Movie with ID %d not found for deletion", movie_id)
        raise HTTPException(status_code=404, detail="Movie not found")
    logger.info("Movie with ID %d deleted successfully", movie_id)
    return {"message": "Movie deleted successfully"}

@router.put("/{movie_id}")
def update_movie(movie_id: int, movie: MovieUpdate, db: Session = Depends(get_db)):
    logger.info("Updating movie with ID: %d", movie_id)
    updated_movie = movie_crud.update_movie(db, movie_id, movie)
    if updated_movie is None:
        logger.error("Movie with ID %d not found for update", movie_id)
        raise HTTPException(status_code=404, detail="Movie not found")
    logger.info("Movie with ID %d updated successfully", movie_id)
    return updated_movie
