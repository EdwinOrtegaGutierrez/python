import datetime
from flask import Flask, jsonify

Ahora = datetime.datetime.now()

file = open("TimePython.txt", "w")

file.write(Ahora.strftime('Fecha: %d/%m/%Y\n\nHora: [%H:%M:%S]'))

file.close()

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def ping():
    return jsonify(Ahora.strftime('Fecha: %d/%m/%Y Hora: [%H:%M:%S]'))

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "3110", debug = True)
