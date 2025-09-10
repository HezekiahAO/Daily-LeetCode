from flask import Flask                                                                                                      # IMPORT STAGE
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Set up your database
db = SQLAlchemy(app)                                               # SET UP STAGE
api = Api(app)   # Thats our Api getting setup


class UserModel(db.Model):   #Creates a database model for users
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)                                                           # SET UP CONTENTS AND CONDITIONS
                                                                                                                                
    def __repr__(self):    # A representational File
        return f'User(name ={self.name}, email = {self.email})'   # A uniue represntation of a user   

# The repr method
#  def __repr__(self):    # A representational File
# return f'User(name ={self.name}, email = {self.email})'   # A uniue represntation of a user donna repr is a better representation of the user medtod
# that tells us how to represtent the object when we print it out.  You know when you run some code and you get something like <User object at 0x7f9c8c0d>
#  that is not very informative. So we use the repr method to give a better representation.
#  So when we print out the object we get something like User(name=John, email=johnbellon@gmail.com)

user_args = reqparse.RequestParser()
user_args.add_argument('name', type = str, required = True, help = 'Name cannot be left Blank chief')
user_args.add_argument('email', type = str, required = True, help = 'Email cannot be left Blank chief')
                    
@app.route("/")   # / gives the home page. TThat right after them come
def home():
    return "Hello Hezekiah, How was your day?"

if __name__ == "__main__":
    app.run(debug=True)

    