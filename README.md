# Flask on Render.com 

This project is intended to help you tie together some important concepts and technologies from the 12-day course, including Git, Flask, JSON, Pandas, Requests, and Bokeh for visualization.  We are hosting our version of this website on Render.com.

There are two branches on this repository.  The `master` branch is a simple Flask application to show a static websitpe.  The [finished example](https://flask-framework.onrender.com) is available online that demonstrates this basic website.

The repository contains a basic template for a Flask configuration that will work on Render.com.

The other branch (`api-altair`)is a skeletal framework that we ask students to fill in during the 12-Day Program.  

## Setup and deploy
- Git clone the existing template repository.
- `requirements.txt` contains some necessary libraries.
- There is some boilerplate HTML code in `templates/`.
- Create the Render.com application through the main dashboard (you want a new "Web Service").
- We know that this will run in Python version 3.9.0.  Specify the Python version on Render by adding an environmental variable called `PYTHON_VERSION` with a value of 3.9.0.
- Once deployed, use the web link provided on the Dahsboard to view the website online.  
- A useful reference for deploying is the Render.com [quickstart guide](https://render.com/docs/deploy-flask).

##  Further references for Flask
- [This article](https://realpython.com/blog/python/python-web-applications-with-flask-part-i/), especially the links in "Starting off".
- [This tutorial](https://github.com/bev-a-tron/MyFlaskTutorial).
