from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import movies_actors as movies_actors_crud
import logging

logger = logging.getLogger()
router = APIRouter()

@router.post("/movies/{movie_id}/actors/{actor_id}")
def add_actor_to_movie(movie_id: int, actor_id: int, db: Session = Depends(get_db)):
    if movie_id <= 0 or actor_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid movie_id or actor_id")
    
    movie = movies_actors_crud.add_actor_to_movie(db, movie_id, actor_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie or Actor not found")
    
    logger.info("Actor %d added to Movie %d", actor_id, movie_id)
    return {"message": "Actor added to movie successfully", "movie": movie}

@router.delete("/movies/{movie_id}/actors/{actor_id}")
def remove_actor_from_movie(movie_id: int, actor_id: int, db: Session = Depends(get_db)):
    if movie_id <= 0 or actor_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid movie_id or actor_id")
    
    movie = movies_actors_crud.remove_actor_from_movie(db, movie_id, actor_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie or Actor not found or not linked")
    
    logger.info("Actor %d removed from Movie %d", actor_id, movie_id)
    return {"message": "Actor removed from movie successfully"}

@router.get("/movies/{movie_id}/actors")
def get_actors_for_movie(movie_id: int, db: Session = Depends(get_db)):
    if movie_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid movie_id")
    
    actors = movies_actors_crud.get_actors_for_movie(db, movie_id)
    if actors is None or len(actors) == 0:
        raise HTTPException(status_code=404, detail="No actors found for this movie")
    
    return actors

@router.get("/actors/{actor_id}/movies")
def get_movies_for_actor(actor_id: int, db: Session = Depends(get_db)):
    if actor_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid actor_id")
    
    movies = movies_actors_crud.get_movies_for_actor(db, actor_id)
    if movies is None or len(movies) == 0:
        raise HTTPException(status_code=404, detail="No movies found for this actor")
    
    return movies
