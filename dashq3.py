from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Use a Bootstrap theme (e.g., 'cerulean')
app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

df = pd.read_csv('https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', on_bad_lines='skip')

fig = px.scatter(df, x='  num_pages', y='average_rating')

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.H1('Dash Application with Bootstrap'),

        html.Div(children='''
            This is an example Dash application with Bootstrap styling.
        '''),

        html.Br(),

        dbc.Row([
            dbc.Col([
                html.Label('Select Feature:', style={'font-weight': 'bold'}),
                dcc.RadioItems(
                    id='radio-choice',
                    options=[
                        {'label': 'Num Pages', 'value': '  num_pages'},
                        {'label': 'Average Rating', 'value': 'average_rating'}
                    ],
                    value='  num_pages',
                    inline=True,
                    style={'display': 'flex', 'flex-direction': 'column', 'font-size': '16px', 'color': '#008000'},
                    labelStyle={'margin-right': '10px'},
                    className='custom-radio'
                ),
            ], md=4),

            dbc.Col([
                html.Label('Select Author:', style={'font-weight': 'bold'}),
                dcc.Dropdown(
                    id='author-dropdown',
                    options=[{'label': author, 'value': author} for author in df['authors'].unique()],
                    multi=True,
                ),
            ], md=4),
        ]),

        html.Br(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='example-graph',
                    figure=fig,
                    style={'backgroundColor': '#ffc0cb'}
                ),
                md=8
            ),
        ]),
    ]
)

@app.callback(
    Output('example-graph', 'figure'),
    [Input('radio-choice', 'value'),
     Input('author-dropdown', 'value')]
)
def update_graph(selected_radio, selected_authors):
    filtered_df = df[df['authors'].isin(selected_authors)] if selected_authors else df

    if selected_radio == '  num_pages':
        fig = px.scatter(filtered_df, x='  num_pages', y='text_reviews_count', title='Num Pages vs Reviews Count')
    elif selected_radio == 'average_rating':
        fig = px.scatter(filtered_df, x='average_rating', y='text_reviews_count', title='Average Rating vs Reviews Count')
    else:
        fig = px.scatter(filtered_df, x='  num_pages', y='text_reviews_count', title='Num Pages vs Reviews Count')
        fig.add_scatter(x=filtered_df['average_rating'], y=filtered_df['text_reviews_count'], mode='markers', marker=dict(color='red'), name='Average Rating')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
