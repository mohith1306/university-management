from backend.models.department_model import add_departments, get_all_departments
def fetch_departments():
    departments = get_all_departments()
    return departments
def add_departments(data):
    department = add_departments(data)
    return department