from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', on_bad_lines='skip')

fig = px.scatter(df, x='  num_pages', y='average_rating')

app = Dash(__name__)

# Layout
app.layout = html.Div(children=[
    html.H1(children='This is an example Dash application for WCS Dash Quest 1'),

    html.Div(children='''
    Grab the code from the previous quest, "Dash Layouts". Create the callback feature. In this case, we need to make the plot reactive to the choices selected in the input components.
    '''),

    html.Br(),

    html.Label('Radio Items'),
    dcc.RadioItems(
        id='radio-choice',
        options=[
            {'label': '  Num Pages', 'value': '  num_pages'},
            {'label': 'Average Rating', 'value': 'average_rating'}
        ]
    ),

    html.Br(),

    html.Label('Select author'),
    dcc.Dropdown(
        id='author-dropdown',
        options=[{'label': author, 'value': author} for author in df['authors'].unique()],
        multi=True
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Callback to update the graph based on user input
@app.callback(
    Output('example-graph', 'figure'),
    [
        Input('radio-choice', 'value'),
        Input('author-dropdown', 'value')
    ]
)
def update_graph(selected_radio, selected_authors):
    filtered_df = df[df['authors'].isin(selected_authors)] if selected_authors else df

    if selected_radio == '  num_pages':
        fig = px.scatter(filtered_df, x='  num_pages', y='text_reviews_count', title='  Num Pages vs Reviews Count')
    elif selected_radio == 'average_rating':
        fig = px.scatter(filtered_df, x='average_rating', y='text_reviews_count', title='Average Rating vs Reviews Count')
    else:
        fig = px.scatter(filtered_df, x='  num_pages', y='text_reviews_count', title='  Num Pages vs Reviews Count')

    return fig

# Call to run the App
if __name__ == '__main__':
    app.run_server(debug=True)
