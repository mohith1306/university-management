from backend.config.db_config import get_db_connection
def get_all_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * from student")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_student(name, dob, student_id, gender, email, phone, address, department_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    if student_id is not None:
        student_id = int(student_id)
    if department_id is not None:
        department_id = int(department_id)
    query = (
        "INSERT INTO student (Student_ID, name, date_of_birth, gender, email, phone, address, department_ID) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    )

    params = (student_id, name, dob, gender, email, phone, address, department_id)
    cursor.execute(query, params)
    connection.commit()
    inserted_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return inserted_id
