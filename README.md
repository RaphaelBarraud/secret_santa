## Secret Santa
HO HO HO Secret Santa Test Project.

The requested features were:
- Creation of a list of participants (DONE)
- Establish a blacklist per participant to prevent certain people from drawing
certain people (API DONE BUT NO FRONTEND)
- Start a draw that allows to get the complete list of relationships ensuring that
each participant receives a gift and has to offer one while taking into account
their potential blacklist (STARTED BUT DID NOT HAVE TIME TO MAKE IT WORK)
- Access the history of the last 5 draws (DONE)

The project was created with the following technologies:
- Backend:
    - Python3/Django
    - SQLite database
- Frontend:
    - Vue.js 3

Having never worked with Django and Vue, there was a lot of learning. It is the main 
reason why I did not manage to go further. It took me more time that the 4 hours
initially planned, but it was interesting for me to try these technos.

When the Backend and Frontend are running, the application is accessible at this address: http://localhost:8080/

## API Documentation
The API Documentaion can be found at this address when the backend is running: http://127.0.0.1:8000/APIDocu
A copy of the documentation is also here: ".\backend\API docu\SECRET SANTA APIs Documentation.yaml"

## Requirements
- Python3 version=3.11
- Node package manager (npm)

## Installation of the development environment for the backend
Please follow these steps to set up the virtual environment for our development framework:
- Open a Terminal and go to the directory where you want to create the virtual environment
- Create the virtual environment with this command: <Python3.11 folder path>/python.exe -m venv .venv
- Activate the virtual environment with this command: .\.venv\Scripts\activate
- Update pip of the virtual environment with this command: python -m pip install --upgrade pip
- Install all dependencies from requirement.txt file with this command: python -m pip install -r requirements.txt
- run this command to create the db.sqlite3 database: python .\backend\secret_santa\manage.py migrate

## Command to use the backend in the development environment
- To run the tests for the APIS:  python .\backend\secret_santa\manage.py test
- To run the backend in the developement environment : python .\backend\secret_santa\manage.py runserver

## Installation of the environment for the frontend
- Open a Terminal and go to the project directory : .\frontend\secret_santa
- Install the environment with this command: npm install

## Command to Compiles and hot-reloads the frontend in the development environment
- npm run serve

## Status
Active

## License
No license.