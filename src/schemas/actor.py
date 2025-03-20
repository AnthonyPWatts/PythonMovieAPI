from pydantic import BaseModel
from typing import Optional

class ActorBase(BaseModel):
    """
    Base schema for Actor. This will be inherited by other Actor-related schemas.
    Contains common attributes for Actor.
    """
    Name: str  # Name of the actor
    BirthDate: str  # Actor's birthdate (string for simplicity)

class ActorCreate(ActorBase):
    """
    Schema for creating an Actor.
    Used when receiving data from the client to create a new Actor.
    """
    pass  # No additional fields are required for creation

class Actor(ActorBase):
    """
    Full Actor schema, including the Actor ID.
    Used for returning Actor data, including the unique ID.
    """
    ID: int  # Actor's unique identifier

    class Config:
        """ Pydantic configuration for ORM compatibility """
        orm_mode = True

class ActorUpdate(ActorBase):
    """
    Schema for updating an Actor.
    Used when receiving data from the client to update an existing Actor.
    """
    pass  # No additional fields are required for updating