import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import flask


server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash 2021"),
        html.Div(children="""Dash: A web application framework for Python."""),
        html.Div(children=[
            html.Div(id='output'),
            html.Button(children='Hello', id='greet'),
        ]),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 5],
                        "type": "bar",
                        "name": u"Montréal",
                    },
                ],
                "layout": {"title": "Dash Data Visualization"},
            },
        ),
    ]
)


@app.callback(
    Output('output', 'children'), [Input('greet', 'n_clicks')]
)
def onclick(n_clicks):
    if n_clicks:
        return "Hello!"
    return ""


if __name__ == "__main__":
    import os

    debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True
    app.run_server(host="0.0.0.0", port=8050, debug=debug)
