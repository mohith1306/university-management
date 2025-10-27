from backend.config.db_config import get_db_connection
def get_all_course():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM classroom")
    course = cursor.fetchall()
    cursor.close()
    connection.close()
    return course
def add_course(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO course (course_id, course_name, credits, department_id, semester) VALUES (%s, %s, %s, %s, %s)",
                   (data['course_id'], data['course_name'], data['credits'], data['department_id'], data['semester']))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message":"Course added uccessfully"}