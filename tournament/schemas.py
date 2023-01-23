from pydantic import BaseModel
from datetime import datetime

class TournamentBase(BaseModel):
  title: str
  description: str
  image: str
  url: str
  categoryId: int
  date: datetime

class TournamentRequest(TournamentBase):
    ...

class TournamentResponse(TournamentBase):
    id: int
    class Config:
        orm_mode = True
