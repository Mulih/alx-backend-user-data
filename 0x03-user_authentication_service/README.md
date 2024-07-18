User Authentication service
This project involves building a user authentication service using Flask and SQLAlchemy in Python. This is a backend-focused project, where you will go through the process of creating an authentication system from scratch for learning purposes. 

Key Learning Objectives\
Declare API routes in a Flask app.
Get and set cookies.
Retrieve request form data.
Return various HTTP status codes.
Project Setup and Requirements
Editors Allowed: vi, vim, emacs.
Interpreter/Compiler: Python 3.7 on Ubuntu 18.04 LTS.
Style Guidelines: Your code must comply with the pycodestyle (version 2.5) style guide.
Documentation: All your modules, classes, and functions must have documentation.
Other Requirements: SQLAlchemy 1.3.x, bcrypt for password hashing, and all files must be executable.
Step-by-Step Tasks
1. User Model
Create a SQLAlchemy model named User for a database table named users. This model should have the following attributes:

id: integer primary key
email: non-nullable string
hashed_password: non-nullable string
session_id: nullable string
reset_token: nullable string
2. Create User
Implement the DB class to handle database operations. Create an add_user method to add a new user to the database.

3. Find User
Implement the find_user_by method in the DB class. This method should take arbitrary keyword arguments and return the first matching user. Raise exceptions if no user is found or if invalid query arguments are provided.

4. Update User
Implement the update_user method in the DB class. This method should update user attributes and save changes to the database.

5. Hash Password
Create a _hash_password method to generate a salted hash of the input password using bcrypt.hashpw.

6. Register User
Implement the Auth.register_user method to handle user registration. If the email is already registered, raise a ValueError.

7. Basic Flask App
Set up a basic Flask app with a single GET route (/) that returns a JSON message {"message": "Bienvenue"}.

8. Register User Endpoint
Create a /users POST endpoint that registers a user with email and password. Return appropriate JSON responses for successful registration or if the email is already registered.

9. Credentials Validation
Implement the Auth.valid_login method to validate user credentials. Use bcrypt.checkpw to verify the password.

10. Generate UUIDs
Create a _generate_uuid function that returns a new UUID as a string.

11. Get Session ID
Implement the Auth.create_session method to create a session for a user and return the session ID.

12. Log In
Create a /sessions POST endpoint for user login. On successful login, create a session and set a session ID cookie.

13. Find User by Session ID
Implement the Auth.get_user_from_session_id method to retrieve a user by session ID.

14. Destroy Session
Implement the Auth.destroy_session method to clear a user's session ID.

15. Log Out
Create a /sessions DELETE endpoint to log out a user by clearing the session ID and redirecting to the home page.

16. User Profile
Create a /profile GET endpoint to return the user's email based on the session ID. Return a 403 status if the session ID is invalid.

Example Usage
Here's an example of how you might test some of the functionalities:

Register a User:
curl -XPOST localhost:5000/users -d 'email=test@example.com' -d 'password=mySecurePassword'

Log In:
curl -XPOST localhost:5000/sessions -d 'email=test@example.com' -d 'password=mySecurePassword' -v

Access Profile:
curl -XGET localhost:5000/profile -b "session_id=<session_id_from_login_response>"
