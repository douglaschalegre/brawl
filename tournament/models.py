from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from datetime import datetime


from database import Base

class Tournament(Base):
    __tablename__ = "tournament"
    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String(100), nullable=False)
    description: str = Column(String(255), nullable=False)
    image: str = Column(String(255), nullable=False)
    url: str = Column(String(255), nullable=True)
    categoryId: int = Column(Integer, ForeignKey("category.id"))
    date: datetime = Column(DateTime, nullable=False)
    createdAt: datetime = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt: datetime = Column(DateTime, nullable=False, onupdate=func.now())
