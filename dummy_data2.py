import sqlite3

def insert_dummy_users():
    conn = sqlite3.connect('Calorie.db')
    cursor = conn.cursor()

    # Dummy data for users
    dummy_users_data = [
        (3, 'password3', 'Bob Smith', 28, 175, 'Male'),
        (4, 'password4', 'Alice Johnson', 35, 165, 'Female'),
        (5, 'password5', 'Charlie Brown', 22, 170, 'Male'),
        # Add more dummy data as needed
    ]

    # Insert dummy data into the users table
    insert_query = "INSERT INTO users (userid, password, name, age, height, gender) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.executemany(insert_query, dummy_users_data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_dummy_users()
