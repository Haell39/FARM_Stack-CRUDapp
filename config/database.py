from pymongo import MongoClient

# Conectando ao MongoDB
client = MongoClient('mongodb://localhost:27017')  
db = client.test  # Selecionar o banco de dados 'test'
