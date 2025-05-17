#!/usr/bin/python3
seed = __import__('seed')


def stream_users_in_batches(batch_size):
    """Yields batches of users from the database."""
    offset = 0
    while True:
        conn = seed.connect_to_prodev()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            break

        yield rows  # ✅ Must use yield, NOT return
        offset += batch_size


def batch_processing(batch_size):
    """Prints users in each batch who are older than 25."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
