import os
import socket


APP_NAME = os.environ['APP_NAME']
HOSTNAME = socket.gethostname()
SECRET_KEY = os.environ['SECRET_KEY']