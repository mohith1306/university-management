from backend.models.classroom_model import add_classroom, get_all_classrooms
def fetch_classrooms():
    classrooms = get_all_classrooms()
    return classrooms
def create_classroom(data):
    classroom = add_classroom(data)
    return classroom