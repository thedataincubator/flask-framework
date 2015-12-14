# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
from flask import Flask,render_template,request

import os
from Quandl import Quandl
import time

import tempfile
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
app_data = Flask(__name__)
app_data.vars={}

@app.route('/')
def main():
 return redirect('index_data')

@app_data.route('/index_data',methods=['GET','POST'])

def index_data():
    
  
    
    if request.method=='GET':
    	return render_template('datarequest.html')
    else:
	# request was a POST
        
	app_data.vars['symbol']=request.form['stock_data']
	
	auth_tok = "VJmYz-1u3Zf6P3ocrkUN"
	string1="WIKI/"
	string2=app_data.vars['symbol']
	string3=string1+string2

	data = Quandl.get(string3, trim_start = "2015-09-01", trim_end = "2015-12-01", authtoken=auth_tok)

	dateaxis = data.reset_index()['Date']
    
	close_data=data['Close']
        x=dateaxis
        y=close_data

        fig=plt.figure()
        axes=fig.add_subplot(1,1,1)
        axes.plot(x, y, marker='.')
        #labels= axes.set_xticklabels(rotation=60, fontsize='small')
        axes.tick_params(axis='x',labelsize=8)
	f=tempfile.NamedTemporaryFile(dir='static/',suffix='png',delete=False)
        plt.savefig(f)
        f.close()
        plotPng=f.name.split('/')[-1]   

        return(render_template('figures.html',y=y, plotPng=plotPng))


if __name__ == '__main__':
    app_data.run(debug=True)
#    app.run(port=33507)
    app.run(host='0.0.0.0')
