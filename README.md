# To-Do List CLI Application

## Problem Statement

**Background:**

In today's busy world, people often need a way to organize and manage their tasks effectively. Whether it's work-related projects, personal errands, or other responsibilities, a to-do list can be a valuable tool. To make task management more convenient, this project aims to develop a command-line interface (CLI) application for creating and managing to-do lists.

**Project Description:**

This project involves creating a To-Do List CLI Application that allows users to add, remove, and list tasks. Users can also add and list users who are responsible for the tasks and categorize tasks into different categories. Additionally, tasks can have priorities and due dates.

**User Stories:**

- As a user, I want to be able to add tasks with titles, descriptions, priorities, and due dates.
- As a user, I want to assign tasks to specific users.
- As a user, I want to categorize tasks into different categories.
- As a user, I want to view a list of tasks, users, and categories.
- As a user, I want to remove tasks when they are completed or no longer needed.

### Installation

1. Clone the repository to your local machine:

   git clone `https://github.com/annndiga/CLI-project.git`

2. Navigate to the project directory:
   `cd ./lib`

3. Install the project dependencies:
    `pipenv install`
    `pipenv install alembic`
    `pipenv install sqlalchemy`
4. Activate the virtual environment:
   `pipenv shell`

## Usage
1. Run the To-Do List CLI Application:
    `python cli.py`

2. Follow the on-screen instructions to interact with the application:

- Add tasks, users, and categories.
- List tasks, users, and categories.
- Remove tasks.
- Quit the application.

## Database
The application uses an SQLite database to store data. The database file is `my_database.db` and will be created automatically when you run the application for the first time.

## Contributing
Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.


## License
This project is licensed under the MIT License - see the LICENSE file for details.
