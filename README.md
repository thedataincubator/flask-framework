# Flask on Heroku

This project is intended to help you tie together some important concepts and
technologies from the 12-day course, including Git, Flask, JSON, Pandas,
Requests, Heroku, and Bokeh/Altair/Plotly for visualization.

The repository contains a basic template for a Flask configuration that will
work on Heroku.

A [finished example](https://lemurian.herokuapp.com) that demonstrates some basic functionality.

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, `conda-requirements.txt`, and `runtime.txt`
  contain some default settings.
- There is some boilerplate HTML in `templates/`
- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.
- (Suggested) Use the [conda buildpack](https://github.com/thedataincubator/conda-buildpack).
  If you choose not to, put all requirements into `requirements.txt`

  `heroku config:add BUILDPACK_URL=https://github.com/thedataincubator/conda-buildpack.git#py3`

  The advantages of conda include easier virtual environment management and fast package installation from binaries (as compared to the compilation that pip-installed packages sometimes require).
  One disadvantage is that binaries take up a lot of memory, and the slug pushed to Heroku is limited to 300 MB. Another note is that the conda buildpack is being deprecated in favor of a Docker solution (see [docker branch](https://github.com/thedataincubator/flask-framework/tree/docker) of this repo for an example).
- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Plot pandas data
- Create an interactive plot from the dataframe. Some recommended libraries: Altair, Bokeh, and Plotly.
- Altair provides a simple interface for creating linked and layered plots. They can even be exported and embedded in static HTML (and remain fully interactive!) See the [documentation](https://altair-viz.github.io/)
  and be sure to check out the example gallery.
- Bokeh can be used in a wide range of applications, from simple charts to extensive dashboards with sophisticated backends. It's the most fully-featured library of these three, but you won't be using it for anything complicated in the Milestone Project. Here you can find the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and some [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Plotly provides a range of APIs in their library. Plotly express, for instance, can be used to create commonly used plots. The Graph Objects API affords more customization, but is more complicated to use. Here is the [documentation](https://plotly.com/python/plotly-express/#gallery) for Plotly Express.
