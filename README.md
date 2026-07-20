# Study Planner

#### Video Demo: <PASTE YOUR YOUTUBE VIDEO URL HERE>

#### Description:

Study Planner is a web application built with Python, Flask, HTML, CSS, and SQLite that helps users organize their study tasks in a simple and user-friendly interface.

The application allows users to create an account, log in securely, and manage their own study tasks. User passwords are securely stored using password hashing, and each user's tasks are separated so that they can only access their own information.

## Features

- User registration
- Secure login and logout
- Add new study tasks
- Display tasks on a personal dashboard
- Store user and task information in a SQLite database
- Simple and responsive interface

## Project Structure

- **app.py** contains the Flask application, routes, and main backend logic.
- **templates/** contains the HTML pages used by Flask, including the login page, registration page, dashboard, and home page.
- **static/style.css** contains the styling for the website.
- **planner.db** is the SQLite database that stores user accounts and tasks.
- **check_db.py** is a small debugging script that prints the contents of the database to verify stored data.
- **requirements.txt** lists the Python packages required to run the project.
- **README.md** provides documentation for the project.

## Design Choices

I chose Flask because it is lightweight and easy to understand while learning web development. SQLite was selected because it integrates well with Flask and is suitable for small projects without requiring a separate database server.

Passwords are hashed before being stored to improve security instead of saving plain text passwords.

The website uses a clean layout with a consistent color palette to make the interface simple and easy to use.

## Challenges

During development, I learned how to:

- Connect Flask with SQLite.
- Implement user authentication.
- Handle sessions to keep users logged in.
- Debug SQL queries and form submissions.
- Organize HTML templates and static files.

This project helped me gain experience in both frontend and backend web development while learning how the different parts of a Flask application work together.