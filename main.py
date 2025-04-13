import dash, dash_bootstrap_components as dbc
import callbacks

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = [
    dash.dcc.Store(id="transition-graph-store"),
    dbc.NavbarSimple(brand="hmm", dark=True, color="dark"),
    dbc.Container([
        dbc.Stack([
            dbc.Card([
                dbc.CardHeader("Input Text"),
                dbc.CardBody([
                    dbc.Textarea(
                        id="input-text-area",
                        placeholder="Enter some text here ...",
                        maxLength=1000,
                        style={"height": "100px"},
                    ),
                ]),
                dbc.CardFooter([
                    dbc.Button("Create Transition Graph", id="create-transition-graph"),
                ]),
            ]),
            dbc.Card([
                dbc.CardHeader("Output Graph"),
                dbc.CardBody([
                    dash.dcc.Graph(id="transition-graph-view"),
                ]),
                dbc.CardFooter([
                    dbc.Button("Generate Text", id="generate-output-text", color="success"),
                ]),
            ]),
            dbc.Card([
                dbc.CardHeader("Generate Text"),
                dbc.CardBody([
                    dbc.Label(id="output-text-area"),
                ]),
            ]),
        ], gap=4),
    ], class_name="py-4"),
]

if __name__ == "__main__":
    app.run()