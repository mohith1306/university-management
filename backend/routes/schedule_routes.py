from flask import Blueprint, jsonify, request
from backend.controllers.schedule_controller import create_schedule, fetch_schedules
schedule_blueprint = Blueprint("schedule_blueprint", __name__)
@schedule_blueprint.route("/schedules",methods=["GET"])
def get_schedules():
    data = fetch_schedules()
    return jsonify(data),200
@schedule_blueprint.route("/schedules",methods=["POST"])
def add_schedule():
    data = request.get_json()
    result = create_schedule(data)
    return jsonify(result),201
