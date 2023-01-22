from pydantic import BaseModel
from datetime import datetime

class CategoryBase(BaseModel):
  id: int
  name: str
  image: str
  createdAt: datetime
  updatedAt: datetime

class CategoryRequest(CategoryBase):
    ...

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode = True
