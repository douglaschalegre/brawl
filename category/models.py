from sqlalchemy import Column, Integer, String, DateTime, func
from datetime import datetime

from database import Base

class Category(Base):
    __tablename__ = "category"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(100), nullable=False)
    image: str = Column(String(255), nullable=False)
    createdAt: datetime = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt: datetime = Column(DateTime, nullable=False, onupdate=func.now())
