from flask import Flask, jsonify, request
from flask_restful import Resource, Api



# creating the flask app/API
app = Flask(__name__)
api = Api(app)

class Suit(Resource):
    
    def get(self, private_player_id):
        
        
