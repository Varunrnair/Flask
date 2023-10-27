from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import cv2
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")
