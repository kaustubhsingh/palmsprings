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
        { "country" : "10-01-2021", "visits" : 20347 },
        { "country" : "17-01-2021", "visits" : 32847 },
        { "country" : "24-01-2021", "visits" : 65542 },
        { "country" : "03-02-2021", "visits" : 75427 },
        { "country" : "10-02-2021", "visits" : 51315 }
    ]

    return render_template('index.html', data=data, chart_data=json.dumps(chart_data))