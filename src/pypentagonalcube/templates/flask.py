"""

    a p i
    API

    A file containing the main definition for our Flask API.

    :requirements:
    pip install flask flask_cors

"""
#
#   :code:

#
#   :packages:
from flask import Flask, request, jsonify
from flask_cors import CORS

#
#   :flask:
app = Flask(__name__)
CORS(app)


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "404, path not found", "path": request.path}), 404


@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": f"{e}", "path": request.path}), 500


#
#   :blueprints:
#   We're using Flask Blueprints to define things, we just need to register them with our application here.
from package.api.blueprints.observations import blueprint_one
active_blueprints = [
    blueprint_one
]
for blueprint in active_blueprints:
    app.register_blueprint(blueprint=blueprint)
