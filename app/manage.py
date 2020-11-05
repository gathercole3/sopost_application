from flask_script import Manager
from src import app
import os

manager = Manager(app)

if __name__ == "__main__":
    manager.run()
