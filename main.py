from flask import Flask, render_template, redirect, url_for, session, request, flash, jsonify, send_from_directory
import json
import db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form.get("pass")
        name = request.form.get("name")

        if password == "rondapulcsi":
            if name:
                result = db.check_name(name)
                if result == "invalid name":
                    return json.dumps({"name": "invalid"})
                elif result == "error":
                    return json.dumps({"name": "error"})
                else:
                    return json.dumps({"name": result})
            else:
                return json.dumps({"name": "noname"})
        else:
            return json.dumps({"name": "wrongpass"})
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
