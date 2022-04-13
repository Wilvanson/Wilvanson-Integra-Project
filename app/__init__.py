
from flask_cors import CORS
from flask import Flask

from .api.data_route import data_routes

app = Flask(__name__)

app.register_blueprint(data_routes, url_prefix='/api/data')

# Application Security
CORS(app)