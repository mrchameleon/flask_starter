# Flask starter app

Template for a flask app, configured with some essentials

* app template, static files
* flask-admin with bootstrap theme (bootswatch united theme)
* sqlalchemy ORM with example User mode
* local sqlite instance for simple DB
* user model and data import script to populate ~1000 user records
* some basic API starter routes, a get and a post
* pytest starter file with two example tests
* gitignore file

### Recommended setup steps

* venv, etc
* `pip install -r requirements.txt`
* `python app.py`
* https://sqlitebrowser.org/ free easy GUI for viewing SQLite records

Home page:
  http://localhost:5000/

Ping endpoint
  GET http://localhost:5000/ping

Post endpoint
  POST http://localhost:5000/post


### to run API tests:
`python -m pytest`
