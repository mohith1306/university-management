from backend.config.db_config import get_db_connection
def get_all_subjects():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM subject")
    subjects = cursor.fetchall()
    cursor.close()
    connection.close()
    return subjects
def add_subject(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO subject (subject_id, subject_name, credits, course_id, faculty_id) VALUES (%s, %s, %s, %s, %s)",
                   (data['subject_id'], data['subject_name'], data['credits'], data['course_id'], data['faculty_id']))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message":"Subject added successfully"}
