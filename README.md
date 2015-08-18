# Flask on Heroku

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, JSON, Pandas,
Requests, Heroku, and Bokeh for visualization.

The repository contains a basic template for a Flask configuration that will
work on Heroku.

A finished example of what your app might look like: `https://lemurian.herokuapp.com`

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- There is some boilerplate html in `templates/`.
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- (Suggested) Use the [conda buildpack](https://github.com/kennethreitz/conda-buildpack).
  If you choose not to, put all requirements into `requirements.txt`.

  `heroku config:add BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git`
- *Question*: What are the pros and cons of using Conda vs. pip?
- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o)

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format.
- Build in some interactivity by having the user submit a form or choose
  from buttons or sliders or something.
- Create a `pandas` dataframe with the data

## Step 3: Use Bokeh to plot pandas data
- Create a Bokeh plot with the data
- Make the plot visible on your website through embedded HTML or other methods...
- Consult the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed)
