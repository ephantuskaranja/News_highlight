from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing my app
app = Flask(__name__, instance_relative_config=True)

# Set up configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# Flask Extensions
bootstrap = Bootstrap(app)

from app import views