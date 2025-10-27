from flask import Blueprint, jsonify, request
from backend.controllers.student_controller import fetch_students, create_student

student_blueprint = Blueprint("student_blueprint", __name__)

@student_blueprint.route("/", methods=["GET"])
def get_students():
    return jsonify(fetch_students())

@student_blueprint.route("/", methods=["POST"])
def add_student():
    data = request.json
    result = create_student(data)
    return jsonify(result), 201
