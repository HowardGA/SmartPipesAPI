from pymongo import MongoClient

mongodb_config = {
    'username': 'BrewIt',
    'password': 'uDd3StzXJ2EdOhG5',
    'database': 'SmartPipes',
    'collection': 'Users',
}

mongo_uri = (
    f"mongodb+srv://{mongodb_config['username']}:{mongodb_config['password']}"
    f"@cluster0.yvhgb38.mongodb.net/{mongodb_config['database']}?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
)
client = MongoClient(mongo_uri)

if (client):
    print("Mongo Connection success")
    
db = client[mongodb_config['database']]
