import psycopg2


# Establising the connection
conn = psycopg2.connect(database="pypractice", user="mayns",
                        password="admin", host='127.0.0.1', port='5432')
conn.autocommit = False

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# SQL Query
# Create database
sql = '''CREATE database pypractice'''

# Drop table if exist
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# Create table
sql = '''CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT
        )'''

# Preparing SQL queries to INSERT a record into the database.
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Mayna', 'Siti', 24, 'F', 9000)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Nami', 'Ayudia', 14, 'F', 6000)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Hurry', 'Muhammad', 20, 'M', 8300)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Angga', 'Perdana', 27, 'M', 10000)''')
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Ika', 'Kartikawati', 24, 'F', 6000)''')

# Retrieving data
cursor.execute('''SELECT * from EMPLOYEE''')

# Where
cursor.execute('''SELECT * from EMPLOYEE WHERE AGE < 25''')

# Order by
cursor.execute('''SELECT * from EMPLOYEE ORDER BY AGE ''')

# Fetching all the rows before the update
print("Contents of the Employee table: ")
sql = '''SELECT * from EMPLOYEE'''
cursor.execute(sql)
print(cursor.fetchall())

# Updating the records
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = 'M'"

# Deleting records
cursor.execute('''DELETE FROM EMPLOYEE WHERE AGE > 25''')
print("Table updated...... ")

# Doping EMPLOYEE table if already exists
cursor.execute("DROP TABLE EMPLOYEE")
print("Table dropped... ")

# Fetching all the rows after the update
print("Contents of the Employee table: ")
sql = '''SELECT * from EMPLOYEE'''


# Limit
sql = '''SELECT * from EMPLOYEE LIMIT 2 OFFSET 2'''

# EXAMPLE FOR INNER JOIN
'''
postgres=# SELECT
 Cricketers.First_Name, Cricketers.Last_Name, Cricketers.Country,
 OdiStats.matches, OdiStats.runs, OdiStats.centuries, OdiStats.halfcenturies
 from Cricketers INNER JOIN OdiStats ON Cricketers.First_Name = OdiStats.First_Name;

'''

# Inner join
sql = '''SELECT * from EMP INNER JOIN CONTACT ON EMP.CONTACT = CONTACT.ID'''
cursor.execute(sql)
print(cursor.fetchall())

# Fetching all row from the table
result = cursor.fetchall()
print(result)

# Fetching 1st row from the table
result = cursor.fetchall()
print(result)

# Commit change in database
conn.commit()
# Closing the connection
conn.close()
