from app.extensions import mongo

def get_all_events():
    return list(mongo.db.events.find())

def add_event(name):
    return mongo.db.events.insert_one({"name": name})
