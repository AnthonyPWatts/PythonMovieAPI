from sqlalchemy.orm import Session
from ..schemas.actor import ActorCreate, ActorUpdate
from ..models import Actor

def get_actors(db: Session):
    """
    Retrieve a list of all actors from the database.
    """
    return db.query(Actor).all()

def get_actor(db: Session, actor_id: int):
    """
    Retrieve a single actor by their ID.
    """
    return db.query(Actor).filter(Actor.ID == actor_id).first()

def create_actor(db: Session, actor: ActorCreate):
    """
    Create a new actor in the database.
    """
    db_actor = Actor(**actor.model_dump())  # Updated for Pydantic v2
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor

def delete_actor(db: Session, actor_id: int):
    """
    Delete an actor by their ID.
    """
    db_actor = db.query(Actor).filter(Actor.ID == actor_id).first()
    if db_actor:
        db.delete(db_actor)
        db.commit()
    return db_actor

def update_actor(db: Session, actor_id: int, actor: ActorUpdate):
    """
    Update an actor and return the updated actor.
    """
    db_actor = db.query(Actor).filter(Actor.ID == actor_id).first()
    if db_actor:
        db_actor.Name = actor.Name
        db_actor.BirthDate = actor.BirthDate
        db.commit()
        # Refresh to ensure that we have the updated data from the DB
        db.refresh(db_actor)
        return db_actor
    return None