# fiasko

fiasko is webapp based on the Flask framework.

## Goal

The goal is to learn Python development with Flask.

## Install

If no venv: `python3 -m venv venv`

Activate: `. venv/bin/activate`

Install Flask if needed: `pip install Flask`

Don't forget to `export FLASK_APP=src/app.py`

## Run

`flask run` or `python app.py`

## DB

```bash
export FLASK_APP=src/manage.py
flask shell
```

then type:

```py
db.create_all()
```
