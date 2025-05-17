#!/usr/bin/python3
import seed
import generator

def main():
    connection = seed.connect_db()
    if connection:
        seed.create_database(connection)
        connection.close()
        print("connection successful")

        connection = seed.connect_to_prodev()
        if connection:
            seed.create_table(connection)
            seed.insert_data(connection, 'user_data.csv')

            # Check database presence
            cursor = connection.cursor()
            cursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';")
            result = cursor.fetchone()
            if result:
                print("Database ALX_prodev is present")

            # Print first 5 rows
            cursor.execute("SELECT * FROM user_data LIMIT 5;")
            rows = cursor.fetchall()
            print(rows)
            cursor.close()

            # Use the generator to stream rows
            print("\nStreaming rows one by one:")
            for row in generator.stream_rows(connection):
                print(row)

            connection.close()

if __name__ == "__main__":
    main()
