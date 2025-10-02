from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #

@main.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    main.run(debug=True)
