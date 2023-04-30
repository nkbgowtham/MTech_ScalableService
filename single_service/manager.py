import mysql.connector


class Authenticator:
    def __init__(self):
        self.myconn = mysql.connector.connect(host="mysql", user="gowtham", passwd="abcd", database="library")
        self.cursor = self.myconn.cursor()

    def __del__(self):
        self.myconn.close()

    def authenticate(self, username, password):
        self.cursor.execute(
            "SELECT * FROM authentication WHERE username = '%s' and password = '%s'" % (username, password))
        result = self.cursor.fetchone()
        if result is None or result == {}:
            return False
        return True


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
