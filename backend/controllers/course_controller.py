from backend.models.course_model import add_course, get_all_course
def fetch_courses():
    courses = get_all_course()
    return courses
def create_course(data):
    course = add_course(data)
    return course