import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.User import User
from models.Task import Task
from models.Category import Category
from models.association import task_category_association  # Import the association table

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
        click.echo(f"User '{username}' added successfully with ID {user.id}")
    except Exception as e:
        session.rollback()
        click.echo(f"Error adding user: {e}")

# Function to add a task
def add_task(user_id, title, description_text, priority, due_date, category_ids):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        try:
            task = Task(
                title=title,
                description=description_text,
                priority=priority,
                due_date=due_date,
                user=user  
            )

            # task to categories if category_ids are provided
            if category_ids:
                categories = session.query(Category).filter(Category.id.in_(category_ids)).all()
                for category in categories:
                    task.categories.append(category)

            session.add(task)  
            session.commit()
            click.echo(f"Task '{title}' added for {user.username}.")
        except Exception as e:
            session.rollback()
            click.echo(f"Error adding task: {e}")
    else:
        click.echo(f"User with ID {user_id} not found.")


# Function to update a task
def update_task(task_id, title=None, description=None, priority=None, due_date=None):
   
    task = session.query(Task).filter(Task.id == task_id).first()

    if not task:
        click.echo("Task not found.")
        return

    # Update task attributes if provided
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if priority is not None:
        task.priority = priority
    if due_date is not None:
        task.due_date = due_date

    
    session.commit()

    click.echo("Task updated successfully.")
# Function to list tasks for a user
def list_tasks(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        if tasks:
            click.echo(f"Tasks for {user.username}:")
            for task in tasks:
                click.echo(f"- {task.title}")
        else:
            click.echo(f"No tasks found for {user.username}.")
    else:
        click.echo(f"User with ID {user_id} not found.")

# Function to list all users
def list_users():
    users = session.query(User).all()
    if users:
        click.echo("List of Users:")
        for user in users:
            click.echo(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        click.echo("No users found.")

# Function to add a category
def add_category(name):
    try:
        category = Category(name=name)
        session.add(category)
        session.commit()
        click.echo(f"Category '{name}' added successfully with ID {category.id}")
    except Exception as e:
        session.rollback()
        click.echo(f"Error adding category: {e}")

# Function to list categories
def list_categories():
    categories = session.query(Category).all()
    if categories:
        click.echo("List of Categories:")
        for category in categories:
            click.echo(f"Category ID: {category.id}, Name: {category.name}")
    else:
        click.echo("No categories found.")

@click.command()
def main():
    while True:
        click.echo("\nTo-Do List Menu:")
        click.echo("1. Add Task")
        click.echo("2. Update Task")
        click.echo("3. Remove Task")
        click.echo("4. List Tasks")
        click.echo("5. Add User")
        click.echo("6. List Users")
        click.echo("7. Add Category")
        click.echo("8. List Categories")
        click.echo("9. Quit")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            user_id = click.prompt("Enter your user ID", type=int)
            title = click.prompt("Enter task title")
            description_text = click.prompt("Enter task description")
            priority = click.prompt("Enter task priority")
            due_date = click.prompt("Enter task due date")
            category_ids = click.prompt("Enter category IDs (comma-separated)", default="").split(',')
            category_ids = [int(cat_id.strip()) for cat_id in category_ids if cat_id.strip()]
            add_task(user_id, title, description_text, priority, due_date, category_ids)
        elif choice == 2:
            task_id = click.prompt("Enter task ID to update", type=int)
            title = click.prompt("Enter updated task title (leave blank to keep current)")
            description = click.prompt("Enter updated task description (leave blank to keep current)")
            priority = click.prompt("Enter updated task priority (leave blank to keep current)")
            due_date = click.prompt("Enter updated task due date (leave blank to keep current)")
            update_task(task_id, title, description, priority, due_date)
        elif choice == 3:
            task_id = click.prompt("Enter task ID to remove", type=int)
            task = session.query(Task).filter_by(id=task_id).first()
            if task:
                session.delete(task)
                session.commit()
                click.echo(f"Task '{task.title}' removed.")
            else:
                click.echo(f"Task with ID {task_id} not found.")
        elif choice == 4:
            user_id = click.prompt("Enter user ID to list tasks", type=int)
            list_tasks(user_id)
        elif choice == 5:
            username = click.prompt("Enter username")
            email = click.prompt("Enter email")
            add_user(username, email)
        elif choice == 6:
            list_users()
        elif choice == 7:
            category_name = click.prompt("Enter category name")
            add_category(category_name)
        elif choice == 8:
            list_categories()
        elif choice == 9:
            
            session.close()
            break
        else:
            click.echo("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
