from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL)

# autocommit=False
# Significa que los cambios no se guardan automáticamente.

# autoflush=False
# Evita que SQLAlchemy envíe cambios automáticamente a la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()