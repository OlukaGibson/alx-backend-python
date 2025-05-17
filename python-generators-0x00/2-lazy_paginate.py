#!/usr/bin/python3
seed = __import__('seed')

def paginate_users(page_size, offset):
    """Fetch a single page of user_data rows with limit and offset"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator to lazily fetch pages of users one by one"""
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
