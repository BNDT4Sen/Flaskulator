# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

#Create an API.

app = Flask(__name__)
api = Api(app)


# Defining classes & endpoints for each operation

class Addition(Resource):
    def post(self):
        json_data = request.get_json()
        num1 = json_data['num1']
        num2 = json_data['num2']
        res = num1 + num2
        return res
class Subtraction(Resource):
    def post(self):
        json_data = request.get_json()
        num1 = json_data['num1']
        num2 = json_data['num2']
        res = num1 - num2
        return res
class Multiplication(Resource):
    def post(self):
        json_data = request.get_json()
        num1 = json_data['num1']
        num2 = json_data['num2']
        res = num1 * num2
        return res
class Division(Resource):
    def post(self):
        json_data = request.get_json()
        num1 = json_data['num1']
        num2 = json_data['num2']
        res = num1 / num2
        return res
    

api.add_resource(Addition, '/addition')
api.add_resource(Subtraction, '/subtraction')
api.add_resource(Multiplication, '/multiplication')
api.add_resource(Division, '/division')


# The last thing to do is to create an application run when the file api.py is run directly (not imported as a module from another script).
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)