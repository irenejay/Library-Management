# Library Management System
The Library Management System  provides functionalities for creating, updating, and deleting authors and books, as well as searching for them based on various criteria. 

The application utilizes Object-Relational Mapping (ORM) techniques to interact with a SQLite database, ensuring data persistence and integrity.


## Features
1.Manage authors: Create, update, delete, and search for authors by name, email, or ID.

2.Manage books: Create, update, delete, and search for books by title or ID.

3.One-to-many relationship: Authors can be associated with multiple books.

4.Command Line Interface (CLI): User-friendly interface for interacting with the application.

5.Input validation: Ensure data integrity by validating user input for author and book creation/update.


## Usage
Ensure the database is initialized and populated with sample data:
python3 debug.py

Run the CLI application:
python3 cli.py

### Follow the prompts to interact with the application:
Choose options to manage authors and books.
Create, update, delete, or search for authors and books as needed.
Use input validation to ensure data integrity.
