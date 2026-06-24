from flask import Flask, render_template, request
from parser import extract_resume_data
from database import create_database, save_candidate
import os

app = Flask(__name__)
create_database()

UPLOAD_FOLDER = "resumes"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    data = None

    if request.method == "POST":
        file = request.files["resume"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            data = extract_resume_data(filepath)
            save_candidate(data)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)