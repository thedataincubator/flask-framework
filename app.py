
# The Data Incubator
# Flask Prep

from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('user_inputs_new.html')

@app.route('/plot',methods=['POST'])
def plot():
    stocksDict = {}
    ticker = request.form['ticker_symbol']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    metric = request.form['metric']

    api_url = ('https://www.quandl.com/api/v3/datatables/WIKI/PRICES?'
               'ticker={0}' # format input
               '&date.gte={1}' # start date
               '&date.lte={2}' # end date
               '&api_key=koLdKmsN94HrPzpnR64z'.format(ticker, start_date, end_date))
    r = requests.get(api_url)
    json_file = r.json()
    stocksDict[ticker] = json_file['datatable']

    colNames = [x['name'] for x in stocksDict[ticker]['columns']]

    # created dictionary of df items, where key is index
    dfDict = {}
    idx_count = 0
    for x in stocksDict:
        for y in stocksDict[x]['data']:
            dfDict[idx_count] = y
            idx_count += 1
        
    # create dataframe
    stocks_df = pd.DataFrame.from_dict(dfDict, orient='index', columns = colNames)
        
    # apply datetime and make index
    stocks_df['date']=pd.to_datetime(stocks_df['date'])
    stocks_df.set_index('date', inplace=True)
        
    input_df = stocks_df[(stocks_df.index >= start_date) &
           (stocks_df.index <= end_date) &
           (stocks_df.ticker == ticker)]

    p = figure(x_axis_type="datetime", title=f"{ticker} Stock Price: {metric}", plot_height=350, plot_width=800)
    p.xgrid.grid_line_color=None
    p.ygrid.grid_line_alpha=0.5 # opacity
    p.xaxis.axis_label = 'Time'
    p.yaxis.axis_label = 'Value'
        
    p.line(input_df.index, input_df[metric])
    script, div = components(p)
    return render_template('plot.html', script=script, div=div)


if __name__ == '__main__':
  app.run(port=33507)