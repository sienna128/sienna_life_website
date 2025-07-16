from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from bson.objectid import ObjectId
from app import mongo

todo_bp = Blueprint('todo', __name__)

@todo_bp.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        due_date = request.form.get("due_date")
        priority = request.form.get("priority")
        date_entered = datetime.now().strftime("%Y-%m-%d")

        if name:
            mongo.db.todos.insert_one({
                "name": name,
                "description": description,
                "date_entered": date_entered,
                "due_date": due_date,
                "priority": priority,
                "completed": False
            })
        return redirect(url_for("todo.todo"))

    todos = list(mongo.db.todos.find())
    return render_template("todo.html", todos=todos)

@todo_bp.route("/todo/toggle/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    todo = mongo.db.todos.find_one({"_id": ObjectId(todo_id)})
    if todo:
        mongo.db.todos.update_one(
            {"_id": ObjectId(todo_id)},
            {"$set": {"completed": not todo.get("completed", False)}}
        )
    return redirect(url_for("todo.todo"))

@todo_bp.route("/todo/delete/<todo_id>", methods=["POST"])
def delete_todo(todo_id):
    mongo.db.todos.delete_one({"_id": ObjectId(todo_id)})
    return redirect(url_for("todo.todo"))
