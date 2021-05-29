from flask import Flask

from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():

    data = [["WEEK", "OUTCOME VARIABLE"], [10/01/2021, 20347],  [17/01/2021, 32847],
     [24/01/2021, 65542], [3/02/2021, 75427], [10/02/2021, 51315],]
    return render_template('index.html', data=data)