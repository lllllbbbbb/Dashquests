from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv',on_bad_lines='skip')

fig = px.scatter(df, x='  num_pages', y='average_rating')

app = Dash(__name__)
# Layout
app.layout = html.Div(children=[
    html.H1(children='This is an example Dash application for WCS Dash Quest 1'),

    html.Div(children='''
        Grab the data from this link. Create a Dash app - no callbacks for now - with at least the following features:

    one graph/plot using the plotly library
    two input (input box, dropdown menu, radio,...) for two different variables that are in the dataset. The type of input has to be decided according to the type of variable you choose.

    '''),

    html.Br(),

    html.Label('Radio Items'),
    dcc.RadioItems(['  num_pages', 'average_rating'], '  num_pages'),


    html.Br(),

    html.Label('Select author'),
    dcc.Dropdown(df.authors.unique(),multi=True),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
# Call to run the App
if __name__ == '__main__':
    app.run_server(debug=True)