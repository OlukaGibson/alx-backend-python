# seed.py
import mysql.connector
import csv
import uuid
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def connect_db():
    """Connect to MySQL server (without specifying DB)"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None


def create_database(connection):
    """Create the ALX_prodev database if not exists"""
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME};")
        connection.commit()
        print(f"Database {DB_NAME} ensured.")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    cursor.close()


def connect_to_prodev():
    """Connect to ALX_prodev database"""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database {DB_NAME}: {err}")
        return None


def create_table(connection):
    """Create user_data table if not exists"""
    cursor = connection.cursor()
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        INDEX (user_id)
    );
    """
    try:
        cursor.execute(create_table_sql)
        connection.commit()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Failed creating table: {err}")
    cursor.close()


def insert_data(connection, filename):
    """Insert data from CSV if user_id does not exist"""
    cursor = connection.cursor()
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            user_id = row.get('user_id')
            # If user_id not provided, generate new UUID
            if not user_id:
                user_id = str(uuid.uuid4())
            name = row.get('name')
            email = row.get('email')
            age = row.get('age')

            # Check if user_id already exists
            cursor.execute("SELECT user_id FROM user_data WHERE user_id=%s;", (user_id,))
            if cursor.fetchone():
                continue  # Skip if exists

            # Insert row
            try:
                cursor.execute(
                    "INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s);",
                    (user_id, name, email, age)
                )
            except mysql.connector.Error as err:
                print(f"Failed to insert row {row}: {err}")

    connection.commit()
    cursor.close()
