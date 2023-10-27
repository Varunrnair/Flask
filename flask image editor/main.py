from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import cv2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

app.run(debug=True)