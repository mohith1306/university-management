from flask import Blueprint, jsonify, request
from backend.controllers.university_controller import fetch_universities, create_university
university_blueprint = Blueprint("university_blueprint", __name__)
@university_blueprint.route("/universities", methods=["GET"])
def get_universities():
    data = fetch_universities()
    return jsonify(data), 200

@university_blueprint.route("/universities", methods=["POST"])
def add_university():
    data = request.get_json()
    result = create_university(data)
    return jsonify(result), 201
