from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(String)  # You can define the appropriate data type for priority
    due_date = Column(String)  # You can define the appropriate data type for due date

    # Define a foreign key column to link tasks to users
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Define a foreign key column to link tasks to categories
    category_id = Column(Integer, ForeignKey('categories.id'))

    # Define the relationships with User and Category
    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")

    def __init__(self, title, description, priority, due_date, user_id, category_id):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.user_id = user_id
        self.category_id = category_id