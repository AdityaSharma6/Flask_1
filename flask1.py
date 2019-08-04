from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/") # Things that are typed into the browser to take you to different pages.
def home():
    return render_template("public/index.html") # Type in the HTML


if __name__ == '__main__':
   app.run(debug = True)