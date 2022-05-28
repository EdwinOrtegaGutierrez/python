from flask import Flask, jsonify

from users import users

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def ping():
    return jsonify({"response": "Hello Word"}) #Convertir un objeto a un Json

@app.route('/users')
def userHanderl():
    return jsonify({"users": users})


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 3110, debug = True)