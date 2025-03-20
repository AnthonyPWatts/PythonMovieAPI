from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database URL, adjust the placeholders with actual credentials and server info
DATABASE_URL = "mssql+pyodbc://SA:<YourStrong!Passw0rd>@host.docker.internal:1433/MoviesDB?driver=ODBC+Driver+17+for+SQL+Server"

# Create the SQLAlchemy engine to connect to the database
engine = create_engine(DATABASE_URL, connect_args={"timeout": 5})

# SessionLocal will be used to create database sessions for each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency function to retrieve a database session.
    
    This function is used in FastAPI to ensure that the database session 
    is opened at the start of the request and closed when done.
    """
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used in the endpoint functions
    finally:
        db.close()  # Ensure the session is closed once done
