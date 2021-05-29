from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():

    data = [["WEEK", "OUTCOME VARIABLE"], [1, 2]]
    return render_template('index.html', data=data)