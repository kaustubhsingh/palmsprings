from flask import Flask

from flask import render_template

import pandas as pd
import numpy as np
from charts.bar_chart import plot_chart
import plotly.graph_objs as go
import plotly.offline as plt



app = Flask(__name__)

@app.route("/")
def index():

    data = [["WEEK", "OUTCOME VARIABLE"], ["10/01/2021", 20347],  ["17/01/2021", 32847],
     ["24/01/2021", 65542], ["03/02/2021", 75427], ["10/02/2021", 51315],]


    trace = go.Bar(x=["10/01/2021", "17/01/2021", "24/01/2021", "03/02/2021", "10/02/2021"],
     y=[20347, 32847, 65542, 75427, 51315])
    layout = go.Layout(title="", xaxis=dict(title="WEEK"),
    yaxis=dict(title="OUTCOME VARIABLE"), )
    data2 = [trace1]
    fig = go.Figure(data=data2, layout=layout)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template('index.html', data=data, plot=fig_json)