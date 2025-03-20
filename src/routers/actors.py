from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.actor import ActorCreate, ActorUpdate
from ..crud import actor as actor_crud
import logging

logger = logging.getLogger()
router = APIRouter()

@router.get("/")
def read_actors(db: Session = Depends(get_db)):
    return actor_crud.get_actors(db)

@router.get("/{actor_id}")
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = actor_crud.get_actor(db, actor_id)
    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.post("/")
def create_actor(actor: ActorCreate, db: Session = Depends(get_db)):
    logger.info("Creating a new actor with name: %s", actor.name)
    return actor_crud.create_actor(db, actor)

@router.delete("/{actor_id}")
def delete_actor(actor_id: int, db: Session = Depends(get_db)):
    logger.info("Attempting to delete actor with ID: %d", actor_id)
    actor = actor_crud.delete_actor(db, actor_id)
    if actor is None:
        logger.warning("Actor with ID %d not found for deletion", actor_id)
        raise HTTPException(status_code=404, detail="Actor not found")
    logger.info("Actor with ID %d deleted successfully", actor_id)
    return {"message": "Actor deleted successfully"}

@router.put("/{actor_id}")
def update_actor(actor_id: int, actor: ActorUpdate, db: Session = Depends(get_db)):
    logger.info("Attempting to update actor with ID: %d", actor_id)
    actor = actor_crud.update_actor(db, actor_id, actor)
    if actor is None:
        logger.warning("Actor with ID %d not found for update", actor_id)
        raise HTTPException(status_code=404, detail="Actor not found")
    logger.info("Actor with ID %d updated successfully", actor_id)
    return actor