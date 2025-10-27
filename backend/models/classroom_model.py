from backend.config.db_config import get_db_connection
def get_all_classrooms():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM classroom")
    classrooms = cursor.fetchall()
    cursor.close()
    connection.close()
    return classrooms
def add_classroom(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO classroom (classroom_id, room_number, building, capacity) VALUES (%s, %s, %s, %s)",
                   (data['classroom_id'], data['room_number'], data['building'], data['capacity']))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message":"Classroom added successfully"}
