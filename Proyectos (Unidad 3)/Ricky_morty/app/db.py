from pymongo import MongoClient

cliente = MongoClient("localhost", 27017)

db=cliente["personajes_flask"] #nombre de mi BBDD
