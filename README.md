# CS217 Assignment 2

**Author**: Bohan Jiang

## Introduction

Based on the functionalities implemented by assignment 1, this assignment adds several functions to it:
1. Enable users to add comments to an existing note
2. Enable delete function for users to delete an existing note
3. Deploy a sqlite database to the backend for query/store data of the note-taking app

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
- `run.py`: main script for running the note-taking app

## Usage
First, activating the python virtual environment and install required packages:
```
source <venv_name>/bin/activate

pip install -r requirements.txt
```

In CLI, run command:
```
python run.py
```

Then, you can complete all functionalities in this web app.

> [!NOTE]
> For creating a new note's title, avoid including slash "/" in the string since the app doesn't parse this case carefully.

