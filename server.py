from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from generator import UserInput, generate_graph

app = Flask(__name__)
api = Api(app)

class Res(Resource):

    def get(self):
        userInput = UserInput.fromRequest(request)
        G = generate_graph(userInput)
        return str(G.edges)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

api.add_resource(Res, "/graph_generator")
app.run(host='0.0.0.0', debug=True) # remove debug=True when finally deploying