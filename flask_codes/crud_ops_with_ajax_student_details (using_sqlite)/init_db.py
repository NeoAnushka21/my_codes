# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('sample_data.db')

# Creating a cursor object using the 
# cursor() method
#cursor = conn.cursor()

# Creating table
table = """CREATE TABLE students_info_(id integer primary key autoincrement ,name VARCHAR(255),department VARCHAR(255),
email VARCHAR(255) unique);"""
conn.execute(table)
print("table created")

# Queries to INSERT records.
conn.execute('''INSERT INTO students_info_(name,department,email) VALUES ('Raju', 'business', 'raju02@gmail.com')''')
conn.execute('''INSERT INTO students_info_(name,department,email)  VALUES ('Shyam', 'accounts', 'shyam02@mail.com')''')
conn.execute('''INSERT INTO students_info_(name,department,email)  VALUES ('Baburao', 'arts', 'baburao02@gmail.com')''')

# Display data inserted
print("Data Inserted in the table: ")
data = conn.execute('''SELECT * FROM students_info_''')
for row in data:
    print(row)

# Commit your changes in the database    
conn.commit()

# Closing the connection
conn.close()
