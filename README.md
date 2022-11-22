# Flask on Render.com 

This project is intended to help you tie together some important concepts and technologies from the 12-day course, including Git, Flask, JSON, Pandas, Requests, and Altair for visualization.  We are hosting our version of this website on Render.com.

There are two branches on this repository.  The `master` branch is a simple Flask application to show a static websitpe.  The [finished example](https://flask-framework.onrender.com) is available online that demonstrates this basic website.

The repository contains a basic template for a Flask configuration that will work on Render.com.

The other branch (`api-altair`)is a skeletal framework that we ask students to fill in during the 12-Day Program.  

Our [finished example](https://flask-framework-ticker.onrender.com/) is available 
online that demonstrates this stock ticker website.

## Setup and deploy
- Git clone the existing template repository.
- `requirements.txt` contains some necessary libraries.  You may need to add more depending upon
how you go about developing your application.
- There is some boilerplate HTML code in `templates/`.
- You will need to alter/add to the provided code to add the additional functionality in Steps 2 and 3 below.  
- Create the Render.com application through the main dashboard (you want a new "Web Service").
- Our version runs in Python version 3.9.0.  On Render, you need to specify this version of Python using
an environment variable called `PYTHON_VERSION` with the value of 3.9.0.  It's easy to do this in the 
Render dashboard when you make your deployment.  
- Once deployed, use the web link provided on the Dahsboard to view the website online.  
- A useful reference for deploying is the Render.com [quickstart guide](https://render.com/docs/deploy-flask).

## Step 2: Get data from API and put it in pandas
- Build in some interactivity by having the user submit a form which determines which data is requested.  We've provided the basic structure of an HTML webpage where a user can submit data.  You will need to capture this submitted data to make a request to the API to retrieve the data you want.  Our version uses the [AlphaVantage](https://www.alphavantage.co/) website to get the stock data.  You can get a free API key from that website.  Other possible sources of this data are also available.    
- Use the `requests` library to grab some data from a public API (as stated, our version uses AlphaVantage). This will
  often be in JSON format, in which case the `json` library will be useful.
- Create a `pandas` DataFrame with the data.

## Step 3: Use Altair or Bokeh to plot pandas data
- Create an Altair plot or Bokeh plot from the DataFrame.
- Consult the Altair [documentation](https://altair-viz.github.io/) or the 
  Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.

## References
- [Flask](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off". 
- [Another Flask tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
