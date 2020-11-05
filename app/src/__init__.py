from flask import Flask

app = Flask(__name__)

app.config.from_pyfile("config.py")
app.secret_key = app.config["SECRET_KEY"]


#these imports must be included after the app object has been created as it is imported in them
from src.blueprints import register_blueprints

# Register any extensions we use into the app
register_blueprints(app)
