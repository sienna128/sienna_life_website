from app import create_app, mongo

app = create_app()

with app.app_context():
    # Delete events missing any of these fields: category, color, date, start_time, end_time
    result = mongo.db.events.delete_many({
        "$or": [
            {"category": {"$exists": False}},
            {"color": {"$exists": False}},
            {"date": {"$exists": False}},
            {"start_time": {"$exists": False}},
            {"end_time": {"$exists": False}}
        ]
    })
    print(f"Deleted {result.deleted_count} old events.")
