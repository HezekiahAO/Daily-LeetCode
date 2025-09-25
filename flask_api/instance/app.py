from flask import Flask                                                                                                      # IMPORT STAGE
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Set up your database
db = SQLAlchemy(app)                                         
api = Api(app)   # Thats our Api getting setup                   # SET UP STAGE



class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'User(name={self.name}, email={self.email})'

user_args = reqparse.RequestParser()
user_args.add_argument('name', type = str, required = True, help = 'Name cannot be left Blank chief')
user_args.add_argument('email', type = str, required = True, help = 'Email cannot be left Blank chief')


user_fields = {   # A dictionary for the fields of a user
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,

}


# Marshal width is a decorator that helps to format the output of a resource in a serialized format


class Users(Resource):   # A class for user resourcess
    @marshal_with(user_fields)
    def get(self):
        users = UserModel.query.all()
        return users


    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel()   # name=args['name'], email = args['email']
        db.session.add(user)
        db.session.commit()
        return user, 201


api.add_resource(Users, '/api/users/')   # /user gives the user page


@app.route("/")   # / gives the home page. TThat right after them come


def home():
    return "Hello Hezekiah, How was your day?"

if __name__ == "__main__":
    app.run(debug=True)