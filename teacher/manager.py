import mysql.connector


class Teacher:
    def __init__(self):
        self.myconn = mysql.connector.connect(host="mysql", user="gowtham", passwd="abcd", database="library")
        self.cursor = self.myconn.cursor()

    def __del__(self):
        self.myconn.close()

    def getTeachers(self):
        self.cursor.execute("SELECT * FROM teacher")
        result = self.cursor.fetchall()
        return result