import sqlite3

# Connect to the SQLite database
db_path = r'D:\smartinternz\Calorie.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert dummy data into the "exercise" table
dummy_data = [
   
  
    (4, 'Swimming', 1, 40, '2023-11-13', 130, 98.3, 350),
    (5, 'Yoga', 1, 60, '2023-11-14', 110, 98.7, 200),
    (6, 'Walking', 1, 45, '2023-11-15', 140, 98.4, 180),
    (7, 'Running', 2, 30, '2023-11-16', 155, 98.8, 320),
    (8, 'Cycling', 2, 45, '2023-11-17', 145, 98.2, 420),
    (9, 'Weightlifting', 1, 60, '2023-11-18', 125, 98.4, 280),
    (10, 'Swimming', 2, 40, '2023-11-19', 135, 98.6, 300)
]

insert_query = '''
    INSERT INTO exercise (exercise_id, exercise_name, userid, duration, date, bpm, temperature, calories)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''

cursor.executemany(insert_query, dummy_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Dummy data added to the 'exercise' table successfully.")
