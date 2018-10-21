from flask import Flask, request
from flask_restful import Resource, Api
import base64

app = Flask(__name__)

api = Api(app)


class ClassName(Resource):
    # @jwt_required()
    def post(self):

        #get input parameters from POST request in json format
        req_data = request.get_json()

        # return output information based on input

        return ({"data":"information"})

    def get(self):
        #return all the information in json form        
        return ({"data":"information"})

api.add_resource(ClassName,"/Link")

app.run(host= ip of api hosting system, port = port_Number, debug = True)
