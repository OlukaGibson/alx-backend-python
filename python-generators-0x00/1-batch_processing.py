#!/usr/bin/python3
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def stream_users_in_batches(batch_size):
    """Generator to fetch user_data rows in batches from DB"""
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)  # fetch a batch of rows
        if not batch:
            break
        yield batch  # yield the batch as a list of dicts

    cursor.close()
    connection.close()

def batch_processing(batch_size):
    """Process batches and yield users with age > 25"""
    for batch in stream_users_in_batches(batch_size):  # loop 1: over batches
        for user in batch:  # loop 2: over users in batch
            if user['age'] > 25:
                yield user  # yield filtered user (generator)
