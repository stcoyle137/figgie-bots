from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import figgie_market



# creating the flask app/API
app = Flask(__name__)
api = Api(app)

h, s_h = figgie_market.generate_hands([figgie_market.Suits.DIAMOND, figgie_market.Suits.HEART, figgie_market.Suits.SPADE, figgie_market.Suits.CLUB],4)



class Hand(Resource):
    
    def get(self, player_id):
        return jsonify(s_h[player_id])
        
        
# adding the defined resources along with their corresponding urls
api.add_resource(Hand, '/hand/<int:player_id>')
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)