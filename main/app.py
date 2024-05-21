from flask import Flask  # Import the Flask class to create a Flask application
from flask_cors import CORS  # Import CORS to enable Cross-Origin Resource Sharing
from flask_restx import Api  # Import Api from Flask-RESTx to structure the RESTful API

from main.routes import configure_routes

app = Flask(__name__)  # Create a Flask application instance
CORS(app)  # Apply CORS to the Flask app to allow cross-origin requests

# Configure the API with a base prefix, version, title, and description
api = Api(app, prefix='/api/v2', version='1.0', title='Assessment Creator', description='Assessment Creator Back-end')


configure_routes(api)  
    # Load configurations, e.g., app.config.from_object('app.config.Config')


def create_app():
   
    return app


if __name__ == '__main__':
    app.run(debug=True)

