# CS217 Assignment 3

**Author**: Bohan Jiang

## Introduction

Based on the functionalities implemented by assignment 2, this assignment wraps existing functionalities
into a docker container.

## File structure
- `/notebook`: python package for running the Flask note-taking app
  - `__init__.py`: the file for initializing and configuring module imports
  - `model.py`: module that contains `SQLAlchemy.ORM` classes
  - `notes.py`: module that interacts with front-end web server and back-end DB
  - `routes.py`: module configuring the Flask web app
- `/instance`: dir that contains database file
- `requirements.txt`: package dependency in desired virtual env
- `/templates`: a directory storing HTML templates for rendering webpages in Flask app
- `/static`: a directory for storing `.css` style sheet for HTML page
- `test.py`: test script for unit-testing `/notebook/notes.py`
- `app.py`: main script for running the note-taking app
- `Dockerfile`: docker file for building an image
- `run.sh`: main script for building and running a docker container

## Usage
- **Step 1**:
In CLI, run command:
```
chmod +x run.sh
./run.sh
```
- **Step 2**:
Then, access the web server using address `localhost:5001`.

> [!NOTE]
> For creating a new note's title, avoid including slash "/" in the string since the app doesn't parse this case carefully.

