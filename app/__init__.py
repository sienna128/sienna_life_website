from flask import Flask
from app.extensions import mongo
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    mongo.init_app(app)

    # Import and register blueprints
    from app.routes.home import home_bp
    from app.routes.calendar import calendar_bp
    from app.routes.workout import workout_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(calendar_bp, url_prefix="/calendar")
    app.register_blueprint(workout_bp, url_prefix="/workout")

    return app