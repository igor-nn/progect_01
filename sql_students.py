
from tabulate import tabulate
import sqlite3

connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
#-------------------------------------------------------создал--CREATE
# query = """CREATE TABLE Students
# (
# Students_Id INTEGER NOT NULL PRIMARY KEY,
# Students_Name TEXT NOT NULL,
# Schol_id INTEGER NOT NULL);"""
#----------------------------------------------------------------------------заполнил--INSERT
# query = """INSERT INTO Students (Students_Id, Students_Name, Schol_id)
# VALUES
# (201, 'Иван', 1),
# (202, 'Пётр', 2),
# (203, 'Анастасия', 3),
# (204, 'Игорь', 4);
# """

# cursor.execute(query)
# connection.commit()
# connection.close()
#------------------------------------------------------------------переименовал--(исправил ошибку)
#
# query = "Alter Table Students RENAME COLUMN Schol_Id TO School_Id "
# cursor.execute(query)
# connection.commit()
#
# -------------------------------------------SELECT
query = """SELECT Students_Id, Students_Name, Students.School_Id, School_Name
           FROM Students 
           LEFT JOIN School 
           ON Students.School_Id = School.School_Id
           WHERE Students_Id = 202
           """
head = ("Students_Id", "Students_Name", "School_Id", "School_Name")

# query = "SELECT Students_Id, Students_Name, School_Id FROM Students WHERE Students_Id = 201 "
# head = ("Students_Id", "Students_Name", "School_Id")

# query  = "SELECT School_Name FROM School WHERE School_Id = 1 "
# head = ("School_Name")

cursor.execute(query)
record = cursor.fetchall()
connection.close()

print(tabulate(record,headers=head, tablefmt="grid"))
