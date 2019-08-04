from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'D:/uploads'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_LENGTH'] = 1024
app.config["ALLOWED_EXTENSIONS"] = ["txt", "docx"]


@app.route("/") # Things that are typed into the browser to take you to different pages.
def home():
    #return ("Hello World!")
    return render_template("public/index.html") 

def allowed_file(filename):
    extension = filename.rsplit(".", 1)[1]
    if not "." in filename:
        return False
    else:
        if extension.lower() in app.config["ALLOWED_EXTENSIONS"]:
            return True
        else:
            return False


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

if __name__ == '__main__':
   app.run(debug = True)