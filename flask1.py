'''
Author: Aditya Sharma
Date: August 1st, 2019
'''

############################################################################################################################################
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import pandas as pd
import os
app = Flask(__name__)
app.config["ALLOWED_EXTENSIONS"] = ["txt", "docx", "pdf"]
app.config['MAX_LENGTH'] = 1024
############################################################################################################################################

def ensure_file(uploaded_file):
    if (uploaded_file == ""):
        return False
    else:
        return True

def ensure_file_extension(uploaded_file):
    if ("." not in uploaded_file):
        return False
    else:
        extension = uploaded_file.rsplit(".", 1)[1]
        if (extension not in app.config["ALLOWED_EXTENSIONS"]):
            return False
        else:
            return True



############################################################################################################################################

@app.route("/home") # When the URL ends with <--, the specified template will be rendered.
def home():
    #return ("Hello World!")
    return render_template("public/index.html") 

@app.route("/upload-file", methods = ["GET", "POST"])
def upload_file():

    if (request.method == "POST"):
        if (request.files):
            user_file = request.files["user_file"]

            if (not ensure_file(user_file.filename)):
                return render_template("public/File_No_Name.html")

            if (not ensure_file_extension(user_file.filename)):
                return render_template("public/Incorrect_Extension.html")

    return render_template("public/upload_file.html")




















'''
def allowed_file(filename):
    extension = filename.rsplit(".", 1)[1]
    if not "." in filename:
        return False
    else:
        if extension.lower() in app.config["ALLOWED_EXTENSIONS"]:
            return True
        else:
            return False
'''
'''
@app.route("/analysis", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if request.files:
            file1 = request.files["file"]
            if (file1.filename == ""):
                print("The file must have a name")
                return redirect(request.url)
            
            if allowed_file(file1.filename):
                print("Wrong file extension. Try again.")
                return redirect(request.url)

            return redirect(request.url)

    #return render_template("public/analysis.html")
'''
if __name__ == '__main__':
   app.run(debug = True)