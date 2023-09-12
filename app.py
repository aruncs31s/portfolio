import os

from flask import (Flask, abort, flash, redirect, render_template, request,
                   session)

# app = Flask(__name__, template_folder="./", static_folder="styles")
app = Flask(__name__)


@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return render_template("index.html")


@app.route("/login", methods=["POST"])
def do_admin_login():
    if request.form["password"] == "password" and request.form["username"] == "admin":
        session["logged_in"] = True
    else:
        flash("wrong password!")
    return home()


#
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4000)
