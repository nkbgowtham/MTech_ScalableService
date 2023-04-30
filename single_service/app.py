import logging
from manager import Authenticator, Student, Teacher


from flask import Flask, request, abort
app = Flask("single_service")


@app.route("/login", methods=['POST'])
def authenticate():
    request_data = request.json
    logging.log(20, request_data)
    username = request_data["username"]
    password = request_data["password"]
    authentication_success = Authenticator().authenticate(username, password)
    if authentication_success:
        return "Success"
    return abort(403)


@app.route("/student", methods=["GET"])
def get_student():
    return Student().getStudents()


@app.route("/teacher", methods=["GET"])
def get_teacher():
    return Teacher().getTeachers()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8003)
