from backend.config.db_config import get_db_connection
def get_all_schedules():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM scheduled_in")
    schedules = cursor.fetchall()
    cursor.close()
    connection.close()
    return schedules
def add_schedule(data):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO scheduled_in (schedule_id, classroom_id) VALUES (%s, %s)",
                   (data['schedule_id'], data['classroom_id']))
    connection.commit()
    cursor.close()
    connection.close()
    return {"Message":"Schedule added successfully"}