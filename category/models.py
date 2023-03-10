from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from datetime import datetime

from database import Base

class Category(Base):
    __tablename__ = "category"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), nullable=False)
    image: str = Column(String(255), nullable=False)
    tournaments = relationship("Tournament", backref="category")
    createdAt: datetime = Column(DateTime, server_default=func.now())
    updatedAt: datetime = Column(DateTime, server_default=func.now(), onupdate=func.now())