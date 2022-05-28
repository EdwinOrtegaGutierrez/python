from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['testore']

coleccion = db['products']

results = coleccion.find()

for i in results:
    print(i['producto'])