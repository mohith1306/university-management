from backend.models.student_model import add_student, get_all_students
def fetch_students():
    students = get_all_students()
    return students
def create_student(data):
    return add_student(data)