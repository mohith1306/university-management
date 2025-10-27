from backend.models.subject_model import add_subject, get_all_subjects
def fetch_subjects():
    subjects = get_all_subjects()
    return subjects
def create_subject(data):
    subject = add_subject(data)
    return subject