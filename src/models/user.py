from sqlalchemy import Column, Integer, String
from src.core.database import Base


# no es obligatorio que todas las columnas de la db esten aca
# El nombre puede ser diferente al que esta en la debe, pero toca hacerlo asi:
# id = Column("userid", Integer, primary_key=True)
class User(Base):
    __tablename__ = "users"
    userid = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
