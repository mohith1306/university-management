from backend.config.db_config import get_db_connection
def get_all_faculties():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM faculty")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_faculty(data):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("INSERT INTO faculty (faculty_id, name, designation, email, phone, department_id) VALUES (%s, %s, %s, %s, %s, %s)",
                   (data['faculty_id'], data['name'], data['designation'], data['email'], data['phone'], data['department_id']))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message":"Faculty added successfully"}
