from backend.models.faculty_model import get_all_faculties, add_faculty
def fetch_all_faculties():
    return get_all_faculties()
def create_faculty(data):
    return add_faculty(data)