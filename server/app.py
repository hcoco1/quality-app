# app.py
from flask import request, session
from flask_restful import Resource

from config import app, db, api # This line will run the config.py file and initialize our app
from models import User

# All routes here!
# Add your model imports


@app.route("/", methods=["GET"])
def root():
	return "<h1>Hello from root!</h1>"

# RESTful route syntax
class Users(Resource):
	def get(self):
		users = [user.to_dict() for user in User.query.all()] # Serialize your users - the password hashes should not be sent to the client
		return users, 200
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
