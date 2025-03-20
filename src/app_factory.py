from fastapi import FastAPI
from .routers import movies, actors, movies_actors

def create_app():
    """ Create and configure the FastAPI app with routes. """
    app = FastAPI()

    # Register routers
    app.include_router(movies.router, prefix="/movies", tags=["movies"])
    app.include_router(actors.router, prefix="/actors", tags=["actors"])
    app.include_router(movies_actors.router, tags=["movies_actors"])

    @app.get("/")
    def root():
        return {"message": "Welcome to the Movies API"}

    return app
