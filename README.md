# Flask-TODO
A minimal TODO app which allows users to add, update and delete tasks. 
(Python version 3.6.9)

**Tech Stack Used**
* Flask 
* SqlAlchmey
* SQLite

**To run**
- For installing all the required files.
```
pip install -r requeriments.txt
```
- To create the initial database, just import the db object from an interactive Python shell and run the SQLAlchemy.create_all() method to create the tables and database
```
>>> from app import db
>>> db.create_all()
```
- To run the app
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```
