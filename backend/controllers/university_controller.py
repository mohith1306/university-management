from backend.models.university_model import add_university, get_all_universities
def fetch_universities():
    universities = get_all_universities()
    return universities
def create_university(data):
    university = add_university(data)
    return university
