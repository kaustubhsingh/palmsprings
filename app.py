from flask import Flask

from flask import render_template

import pandas as pd
import numpy as np
import json





app = Flask(__name__)

@app.route("/")
def index():

    data = [["WEEK", "OUTCOME VARIABLE"], ["10/01/2021", 20347],  ["17/01/2021", 32847],
     ["24/01/2021", 65542], ["03/02/2021", 75427], ["10/02/2021", 51315]]

    chart_data = [
        { "week" : "10-01-2021", "outcome" : 20347 },
        { "week" : "17-01-2021", "outcome" : 32847 },
        { "week" : "24-01-2021", "outcome" : 65542 },
        { "week" : "03-02-2021", "outcome" : 75427 },
        { "week" : "10-02-2021", "outcome" : 51315 }
    ]

    return render_template('index.html', data=data, chart_data=json.loads(chart_data))