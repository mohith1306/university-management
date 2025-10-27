from flask import Blueprint, jsonify, request
from backend.controllers.classroom_controller import fetch_classrooms, create_classroom
classroom_blueprint = Blueprint("classroom_blueprint", __name__)
@classroom_blueprint.route("/classrooms",methods=["GET"])
def get_classrooms():
    data = fetch_classrooms()
    return jsonify(data),200
@classroom_blueprint.route("/classrooms",methods=["POST"])
def add_classroom():
    data = request.get_json()
    result = create_classroom(data)
    return jsonify(result),201
