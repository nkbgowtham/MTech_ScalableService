from flask import Flask
from manager import Student

app = Flask("student")


@app.route("/student", methods=["GET"])
def get_student():
    return Student().getStudents()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)
