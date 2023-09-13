from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from .association import task_category_association  # Import the association table

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(String)
    due_date = Column(String)

    # a foreign key column to link tasks to users
    user_id = Column(Integer, ForeignKey('users.id'))

    #  many-to-one relationship with User
    user = relationship("User", back_populates="tasks")

    # many-to-many relationship with Category using the association table
    categories = relationship("Category", secondary=task_category_association, back_populates="tasks")

    def __init__(self, title, description, priority, due_date, user):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.user = user 