from pymongo import MongoClient
connection = MongoClient('localhost', 27017) # Connect to MongoDB

#db = connection['test'] # Get a database
# Or --> db = connection.test # Get a database

connection = MongoClient('mongodb://localhost:27017/test') # Connect to MongoDB and get a database (test)





