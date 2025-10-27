from flask import Blueprint, jsonify, request
from backend.controllers.subject_controller import create_subject, fetch_subjects
subject_blueprint = Blueprint("subject_blueprint", __name__)
@subject_blueprint.route("/subjects",methods=["GET"])
def get_subjects():
    data = fetch_subjects()
    return jsonify(data),200
@subject_blueprint.route("/subjects",methods=["POST"])
def add_subject():
    data = request.get_json()
    result = create_subject(data)
    return jsonify(result),201
