from sqlalchemy import Table, Column, Integer, ForeignKey
from base import Base

# Define the association table
task_category_association = Table(
    'task_category_association',
    Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)
