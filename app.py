from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():

    #data = [["x", "y"], [1, 2]]
    return render_template('index.html', data = [1, 2, 3, 4])