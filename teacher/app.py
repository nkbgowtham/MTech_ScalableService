from flask import Flask
from manager import Teacher

app = Flask("teacher")


@app.route("/teacher", methods=["GET"])
def get_teacher():
    return Teacher().getTeachers()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8002)
