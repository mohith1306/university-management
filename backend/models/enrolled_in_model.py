from backend.config.db_config import get_db_connection
def get_all_enrollments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM enrolled_in")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_enrollments(data):
    """
    Insert an enrollment row. Normalizes integer-like fields and returns the inserted row id.

    Expected keys in data: enrollment_id, student_id, course_id, enrollment_date, grade
    """
    connection = get_db_connection()
    cursor = connection.cursor()

    # Normalize integer fields (will raise ValueError if invalid)
    enrollment_id = data.get('enrollment_id')
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    if enrollment_id is not None:
        enrollment_id = int(enrollment_id)
    if student_id is not None:
        student_id = int(student_id)
    if course_id is not None:
        course_id = int(course_id)

    enrollment_date = data.get('enrollment_date')
    grade = data.get('grade')

    query = ("INSERT INTO enrolled_in (enrollment_id, student_id, course_id, enrollment_date, grade) "
             "VALUES (%s, %s, %s, %s, %s)")

    params = (enrollment_id, student_id, course_id, enrollment_date, grade)
    cursor.execute(query, params)
    connection.commit()
    inserted_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return {"inserted_id": inserted_id}
