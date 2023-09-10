from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define a one-to-many relationship with Task
    tasks = relationship("Task", back_populates="category")

    def __init__(self, name):
        self.name = name