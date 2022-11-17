# Flask on Render.com 

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, JSON, Pandas,
Requests, and Bokeh for visualization.  We are hosting our version of this 
website on Render.com.

There are several branches on this repository.  The `master` branch is a simple
Flask application to show a static websitpe.  The 
[finished example](https://flask-framewy1ork.onrender.com) is available 
online that demonstrates this basic website.

The repository contains a basic template for a Flask configuration that will
work on Render.com.

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `requirements.txt` contains some necessary libraries.
-  We know that this will run in Python version 3.9.0.
- There is some boilerplate HTML code in `templates/`.
- Create the Render.com application through the main dashboard (you want a new "Web Service").
- Specify the Python version on Render by adding an environmental variable called `PYTHON_VERSION` with a value of 3.9.0.
- Once deployed, use the web link provided on the Dahsboard to view the website online.  
- A useful reference for deploying is the Render.com [quickstart guide](https://render.com/docs/deploy-flask).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Use Bokeh to plot pandas data
- Create a Bokeh plot from the dataframe.
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Make the plot visible on your website through embedded HTML or other methods - this is where Flask comes in to manage the interactivity and display the desired content.
- Some good references for Flask: [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off", and [this tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
