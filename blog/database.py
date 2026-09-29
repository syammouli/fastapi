from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# BASE_URL = 'sqlite:///./blog.db'

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# New PostgreSQL connection
# Format: postgresql://[user]:[password]@[postgresserver]/[db_name]
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg://postgres:123456@localhost:5432/blog_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()