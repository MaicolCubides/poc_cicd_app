from pydantic import BaseModel, Field

# Mientras SQLAlchemy representa la base de datos, Pydantic representa los datos que entran y salen de tu API.

class UserBase(BaseModel):
    name: str = Field(..., min_length=2) # ... significa que es requerido
    age: int = Field(..., ge=0)

# Hereda de UserBase
class UserCreate(UserBase):
    pass

# Este schema se usa cuando la API response age y name
class UserResponse(UserBase):
    # y agregamos userid
    userid: int

# Convierte objetos ORM en JSON
    class Config:
        from_attributes = True