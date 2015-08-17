# Flask on Heroku

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, json, pandas,
requests, Heroku, and Bokeh for visualization.

The repository contains a basic template for a Flask configuration that will
work on Heroku.

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- There is some boilerplate html in `templates/`.
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- (Suggested) Use the conda buildpack. If you choose not to, put all requirements
  into `requirements.txt`. Question: What are the pros and cons of using Conda
  vs. pip?
  `heroku config:add BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git`
- Deploy to Heroku: `git push heroku master`
- Take a look with `heroku open`

## Step 2: Get data from API and put it in pandas

## Step 3: Use Bokeh to plot pandas data
