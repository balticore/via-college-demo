from flask import Flask
from flask_restful import Resource, Api
import socket

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return f"Hostname: {socket.gethostname()}"

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
