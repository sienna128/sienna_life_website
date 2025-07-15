from flask import Blueprint, render_template, request, redirect, url_for
from app import mongo

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route("/", methods=["GET", "POST"])
def calendar():
    if request.method == "POST":
        event_name = request.form.get("name")
        category = request.form.get("category")
        color = request.form.get("color")
        date = request.form.get("date")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")

        if event_name and date and start_time and end_time:
            mongo.db.events.insert_one({
                "name": event_name,
                "category": category,
                "color": color,
                "date": date,
                "start_time": start_time,
                "end_time": end_time
            })
        return redirect(url_for("calendar.calendar"))

    events = list(mongo.db.events.find())
    return render_template("calendar.html", events=events)
