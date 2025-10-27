from backend.models.enrolled_in_model import add_enrollments, get_all_enrollments
def fetch_enrollments():
    result = get_all_enrollments()
    return result
def create_enrollment(data):
    enrollment = add_enrollments(data)
    return enrollment