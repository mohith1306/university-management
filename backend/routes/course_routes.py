from flask import Blueprint, jsonify, request
from backend.controllers.course_controller import fetch_courses, create_course
course_blueprint = Blueprint("course_blueprint",__name__)
@course_blueprint.route("/courses",methods=["GET"])
def get_course():
    data = fetch_courses()
    return jsonify(data),200
@course_blueprint.route("/courses",methods=["POST"])
def add_course():
    data = request.get_json()
    result = create_course(data)
    return jsonify(result),201