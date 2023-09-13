from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models.User import User
from lib.models.Task import Task
from lib.models.Category import Category

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///my_database.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a user
def add_user(username, email):
    try:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        return user
    except Exception as e:
        session.rollback()
        raise e

# Function to add a task
def add_task(user_id, title, description, priority, due_date, category_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        try:
            task = Task(
                title=title,
                description=description,
                priority=priority,
                due_date=due_date,
                category_id=category_id,
                user_id=user.id,
            )
            session.add(task)
            session.commit()
            return task
        except Exception as e:
            session.rollback()
            raise e
    else:
        raise ValueError(f"User with ID {user_id} not found.")

# Function to list tasks for a user
def list_tasks(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        return tasks
    else:
        raise ValueError(f"User with ID {user_id} not found.")

# Function to add a category
def add_category(name):
    try:
        category = Category(name=name)
        session.add(category)
        session.commit()
        return category
    except Exception as e:
        session.rollback()
        raise e

# Function to list categories
def list_categories():
    categories = session.query(Category).all()
    return categories

def run_tests():
    # Test adding a user
    user = add_user("test_user", "test@example.com")
    assert user.username == "test_user"
    assert user.email == "test@example.com"

    # Test adding a task
    task = add_task(user.id, "Test Task", "Description", "High", "2023-09-15", 1)
    assert task.title == "Test Task"
    assert task.description == "Description"

    # Test listing tasks for a user
    tasks = list_tasks(user.id)
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"

    # Test adding a category
    category = add_category("Test Category")
    assert category.name == "Test Category"

    # Test listing categories
    categories = list_categories()
    assert len(categories) == 1
    assert categories[0].name == "Test Category"

    print("All tests passed.")

if __name__ == '__main__':
    run_tests()