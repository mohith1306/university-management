import backend
from flask import Flask
from flask_cors import CORS
from backend.routes.university_routes import university_blueprint
from backend.routes.student_routes import student_blueprint
from backend.routes.classroom_routes import classroom_blueprint
from backend.routes.course_routes import course_blueprint
from backend.routes.department_routes import department_blueprint
from backend.routes.enrolled_routes import enrolled_blueprint
from backend.routes.faculty_routes import faculty_blueprint
from backend.routes.subject_routes import subject_blueprint
from backend.routes.schedule_routes import schedule_blueprint
app = Flask(__name__)
CORS(app)
app.register_blueprint(university_blueprint, url_prefix="/api")
app.register_blueprint(student_blueprint, url_prefix="/api")
app.register_blueprint(classroom_blueprint, url_prefix="/api")
app.register_blueprint(course_blueprint, url_prefix="/api")
app.register_blueprint(department_blueprint, url_prefix="/api")
app.register_blueprint(enrolled_blueprint, url_prefix="/api")
app.register_blueprint(faculty_blueprint,url_prefix="/api")
app.register_blueprint(subject_blueprint,url_prefix="/api")
app.register_blueprint(schedule_blueprint,url_prefix="/api")
@app.route("/")
def home():
    return {"message": "University Management System API is running"}

if __name__ == "__main__":
    app.run(debug=True)
