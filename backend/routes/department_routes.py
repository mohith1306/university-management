from flask import Blueprint, jsonify, request
from backend.controllers.department_controller import fetch_departments, add_departments
department_blueprint = Blueprint("department_blueprint",__name__)
@department_blueprint.route("/departments",methods=["GET"])
def get_departments():
    data  = fetch_departments()
    return jsonify(data),200
@department_blueprint.route("/departments", methods=["POST"])
def add_department():
    data = request.get_json()
    result = add_departments(data)
    return jsonify(result), 201
