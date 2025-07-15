# app/routes/workout.py
from flask import Blueprint, render_template, request, redirect, url_for
from app import mongo

workout_bp = Blueprint('workout', __name__)

@workout_bp.route("/workout", methods=["GET", "POST"])
def workout():
    if request.method == "POST":
        exercise = request.form.get("exercise")
        date = request.form.get("date")
        sets = request.form.get("sets")
        reps = request.form.get("reps")
        notes = request.form.get("notes")

        if exercise and date:
            mongo.db.workouts.insert_one({
                "exercise": exercise,
                "date": date,
                "sets": sets,
                "reps": reps,
                "notes": notes
            })
        return redirect(url_for("workout.workout"))

    logs = list(mongo.db.workouts.find())
    return render_template("workout.html", logs=logs)
