from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from send_email import send_email
from sqlalchemy.sql import func
import pandas as pd
import csv

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://cajyuwzkxohgyb:033291c3b3643ae5c2508dc314580a7f30bbf944551810359b2da4b31f42506e@ec2-34-225-167-77.compute-1.amazonaws.com:5432/d7ntc0v4jfgge6?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method == 'POST':
        file = request.files["file"]
        file.save(secure_filename("uploaded"+file.filename))
        with open("uploaded"+file.filename, "a") as f:
            f.write("This was added later!")
        with open('employee_file.csv', mode='w') as employee_file:
            employee_writer = csv.writer(employee_file)
            print(type(employee_writer))
            print(employee_writer)
        return render_template("index.html", btn="download.html")


@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == "__main__":
    app.debug = True
    app.run()
