from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from Weather.rain import get_rain_data, get_rain_interpolation
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 


class RainDate(Resource):
    def get(self):
        rain = get_rain_data(-20, -44)
        return jsonify(rain)


class RainInter(Resource):
    def get(self):
        data = get_rain_interpolation(-23.4188195, -46.638587)
        return jsonify(data)


api.add_resource(RainDate, '/rain')
api.add_resource(RainInter, '/rainInter')
api.add_resource(Employees, '/employees') # Route_1

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

