# CS217 Assignment 1

**Author**: Bohan Jiang

## Introduction

The assignment implements three web services interacting with a note-taking app. The services are `Flask`, `FastAPI` and `Streamlit`.

This note-taking app achieves fundamental behaviors including:
- See all notes with their names
- See the content of a specific note
- Search for a specific note by providing a term might be in
- Add a new note
- Clear the notebook

## File structure
- `notes.py`: the standalone notebook module for APIs to interact with
- `api.py`: FastAPI implementation
- `app.py`: Flask implementation
- `stream.py`: Streamlit implementation
- `requirements.txt`: package dependency in desired virtual env
- `/templates`: a directory storing HTML templates for rendering webpages in Flask app
- `/static`: a directory for storing `.css` style sheet for HTML page
- `/test`: a directory for unit-testing `notes.py`

## Usage
Before running, create a python virtual environment and activate it. Then, run below:
```
pip install -r requirements.txt
```

For running FastAPI, users can proceed interactions either in web or CLI using `curl`:

For example, to list all existing notes in current notebook:
```
http://127.0.0.1:8000/list  # visit this local host

curl http://127.0.0.1:8000/list  # by curl
```

In particular, for adding a note, this is a POST request, users should use `curl` for updating the status of the app:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Mon",
  "contents": "Today is monday, but it is rainy."
}'
```

In addition, for running Flask web app, in CLI run:
```
python app.py
```

or for Streamlit app, please run:
```
streamlit run stream.py
```

Then, you can complete all functionalities in this web app.

> [!NOTE]
> For the very first time, no any note has been added. Simply add a new note to see the change of the site.

