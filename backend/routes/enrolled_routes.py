from flask import Blueprint, request, jsonify
from backend.controllers.enrolled_controller import fetch_enrollments, create_enrollment
enrolled_blueprint = Blueprint("enrolled_blueprint",__name__)
@enrolled_blueprint.route("/enrollments",methods=["GET"])
def get_enrollments():
    data = fetch_enrollments()
    return jsonify(data),200
@enrolled_blueprint.route("/enrollments",methods=["POST"])
def add_enrollment():
    data = request.get_json()
    result = create_enrollment(data)
    return jsonify(result),201