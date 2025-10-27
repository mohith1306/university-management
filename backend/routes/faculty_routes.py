from flask import Blueprint, jsonify, request
from backend.controllers.faculty_controller import fetch_all_faculties, create_faculty
faculty_blueprint = Blueprint("faculty_blueprint", __name__)
@faculty_blueprint.route("/faculties",methods=["GET"])
def get_faculties():
    data = fetch_all_faculties()
    return jsonify(data),200
@faculty_blueprint.route("/faculties",methods=["POST"])
def add_faculty():
    data = request.get_json()
    result = create_faculty(data)
    return jsonify(result),201