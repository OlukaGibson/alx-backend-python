# generator.py

def stream_rows(connection):
    """Generator to stream rows one by one from user_data table"""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")

    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row

    cursor.close()
