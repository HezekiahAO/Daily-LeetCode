from flask import Flask                                                                                                      # IMPORT STAGE
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort 
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # maps your relative path to the database
db = SQLAlchemy(app)                                               # SET UP STAGE
api = Api(app)   # Thats our Api getting setup


with app.app_context():  #This creates the database
    db.create_all()


class UserModel(db.Model):   # Creates a database model for users
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)                                                           # SET UP CONTENTS AND CONDITIONS

    def __init__(self, email, name):
        self.name = name
        self.email = email

    def __repr__(self):    # A representational File
        return f'User(name ={self.name}, email = {self.email})'   # A uniue represntation of a user   

# The repr method
#  def __repr__(self):    # A representational File
# return f'User(name ={self.name}, email = {self.email})'   # A uniue represntation of a user donna repr is a better representation of the user medtod
# that tells us how to represtent the object when we print it out.  You know when you run some code and you get something like <User object at 0x7f9c8c0d>
#  that is not very informative. So we use the repr method to give a better representation.
#  So when we print out the object we get something like User(name=John, email=johnbellon@gmail.com)

user_args = reqparse.RequestParser()
user_args.add_argument('name', type = str, required = True, help = 'Name cannot be left Blank chief', location = 'json')
user_args.add_argument('email', type = str, required = True, help = 'Email cannot be left Blank chief', location = 'json')

user_fields = { 
    'id': fields.Integer,
    'name': fields.String,                # Serialization fields for the user model
    'email': fields.String
}


class Users(Resource):   # This is a resource for a single user  
    @marshal_with(user_fields)   # This is a decorator that will serialize the output of the get method (Translate to something you can understand)
    def get(self):
        users = UserModel.query.all()   # This gets all the users from the database 
        return users

    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()   
        user = UserModel(name=args['name'], email=args['email'])
        db.session.add(user)
        db.session.commit()
        return user, 201
        

class User(Resource):
        @marshal_with(user_fields)
        def get(self, id):
            user = UserModel.query.filter_by(id=id).first()
            if not user: 
                abort(404, help = 'User not Found')
                return user



api.add_resource(Users, '/api/users')   # This adds the resource to the api
                    
@app.route("/")   # / gives the home page. TThat right after them come
def home():
    return "Hello Hezekiah, How was your day?"

if __name__ == "__main__":
    app.run(debug=True)