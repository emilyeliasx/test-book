# Interactive Visualisation Example

This is showing how an interactive visualisation could work for Jupyter Book - this page is a `.ipynb` page rather than a `.md` page.

import plotly.io as pio
import plotly.express as px
import plotly.offline as py

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="sepal_length")
fig

