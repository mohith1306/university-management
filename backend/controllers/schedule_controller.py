from backend.models.scheduled_in_model import get_all_schedules, add_schedule
def fetch_schedules():
    return get_all_schedules()
def create_schedule(data):
    return add_schedule(data)