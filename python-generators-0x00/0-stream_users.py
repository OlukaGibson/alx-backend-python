#!/usr/bin/python3
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def stream_users():
    """Generator that yields user_data rows one by one as dictionaries"""

    # Connect to ALX_prodev database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor(dictionary=True)  # dictionary=True yields dict rows

    cursor.execute("SELECT * FROM user_data;")

    # One loop to fetch and yield rows
    for row in cursor:
        yield row

    cursor.close()
    connection.close()
