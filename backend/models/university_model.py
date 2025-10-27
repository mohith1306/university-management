from backend.config.db_config import get_db_connection
def get_all_universities():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary = True)
    cursor.execute("SELECT * FROM university")
    universities = cursor.fetchall()
    cursor.close3()
    connection.close()
    return universities
def add_university(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.excute("INERT INTO university (university_id, name, etablished_year, location) VALUES (%s, %s, %s, %s)")
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message": "University added successfully"}

    