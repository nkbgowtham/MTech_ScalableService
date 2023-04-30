import mysql.connector


class Student:
    def __init__(self):
        self.myconn = mysql.connector.connect(host="mysql", user="gowtham", passwd="abcd", database="library")
        self.cursor = self.myconn.cursor()

    def __del__(self):
        self.myconn.close()

    def getStudents(self):
        self.cursor.execute("SELECT * FROM student")
        result = self.cursor.fetchall()
        return result