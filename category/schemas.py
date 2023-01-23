from pydantic import BaseModel
from datetime import datetime

class CategoryBase(BaseModel):
  name: str
  image: str

class CategoryRequest(CategoryBase):
    ...

class CategoryResponse(CategoryBase):
    id: int
    class Config:
        orm_mode = True
