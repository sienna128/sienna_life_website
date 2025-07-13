from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# MongoDB URI from Atlas
app.config["MONGO_URI"] = "mongodb+srv://314sienna:wS266073@siennacluster.j8ez2b0.mongodb.net/sienna_life?retryWrites=true&w=majority&appName=SiennaCluster"
mongo = PyMongo(app)
print(mongo.db)

try:
    mongo.db.list_collection_names()
    print("Successfully connected and authenticated!")
except Exception as e:
    print("Error authenticating:", e)

@app.route("/", methods=["GET", "POST"])
def calendar():
    if request.method == "POST":
        event_name = request.form.get("event")
        if event_name:
            mongo.db.events.insert_one({"name": event_name})
        return redirect("/")

    events = mongo.db.events.find()
    return render_template("calendar.html", events=events)

if __name__ == "__main__":
    app.run(debug=True)

