from backend.config.db_config import get_db_connection
def get_all_departments():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM department")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
def add_departments(data):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("INSERT INTO department (department_id, name, building, hod_id, university_id) VALUES (%s, %s, %s, %s, %s)",
                   (data['department_id'], data['name'], data['building'], data['hod_id'], data['university_id']))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message":"Department added successfully"}
