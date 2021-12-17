from flask import Flask, request, render_template
import pandas as pd
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    req = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=04fb8fc6ae8e62e2d9ba10c8a087985b')
    mydata = json.loads(req.content)
    df = pd.DataFrame(mydata)
    df2 = df.reset_index()
    data1 = df2.rename({'index': 'Country'}, axis='columns')
    return render_template('index.html', tables=[data1.to_html(classes='female')],
                           titles=['Country', 'success', 'timestamp', 'base', 'date', 'rates'])


@app.route('/visual')
def google_pie_chart():
    return render_template('visual.html')


# @app.route('/visual', methods=['GET', 'POST'])
# def visual():
#   return render_template('visual.html')


if __name__ == '__main__':
    app.run()
