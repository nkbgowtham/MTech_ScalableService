import logging
from manager import Authenticator


from flask import Flask, request, abort
app = Flask("authentication")


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8000)
