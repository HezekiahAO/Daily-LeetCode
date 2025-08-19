# this is a simple python project aimed to impplement my practical knowledge in Backend
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime as date_time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'# database URI   //// is an absolute path to the database file and /// is a relative path of that data base

#Data Base
db = SQLAlchemy(app) # SQLAlchemy is an ORM (Object Relational Mapper) that allows us to interact with the database using Python objects instead of SQL queries.

class Todo:(db.Model)
id = db.Column(db.Integer, primary_key=True)
content = db.Column(db.String(200), nullable=False) # We dont want the user to create a todo task and leaveit empty.
date_time = db.column(db.DateTime) # This will automatically set the date and time when the task is created.
def __repr__(self):
        return f'<Task {self.id}>' # This will return the id of the task when printed

@app.route("/")
def home():
    return render_template("index.html")   # must match filename

if __name__ == "__main__":
    app.run(debug=True)
