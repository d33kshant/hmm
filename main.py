import dash, dash_bootstrap_components as dbc
import callbacks

# ⚠ This project uses the lyrics of "Blowin’ in the Wind"
# by Bob Dylan for educational purposes only. I do not 
# claim ownership of the song.
lyrics = """
How many roads must a man walk down
Before you call him a man?
How many seas must a white dove sail
Before she sleeps in the sand?
Yes, and how many times must the cannonballs fly
Before they're forever banned?
The answer, my friend, is blowin' in the wind
The answer is blowin' in the wind
Yes, and how many years must a mountain exist
Before it is washed to the sea?
Yes, and how many years can some people exist
Before they're allowed to be free?
Yes, and how many times can a man turn his head
And pretend that he just doesn't see?
The answer, my friend, is blowin' in the wind
The answer is blowin' in the wind
Yes, and how many times must a man look up
Before he can see the sky?
Yes, and how many ears must one man have
Before he can hear people cry?
Yes, and how many deaths will it take 'til he knows
That too many people have died?
The answer, my friend, is blowin' in the wind
The answer is blowin' in the wind
"""

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = [
    dash.dcc.Store(id="transition-graph-store"),
    dbc.NavbarSimple(brand="hmm", dark=True, color="dark"),
    dbc.Container([
        dbc.Alert(
            '⚠ This project uses the lyrics of "Blowin’ in the Wind" by Bob Dylan for educational purposes only. I do not claim ownership of the song.',
            dismissable=True,
            color="warning",
        ),
        dbc.Stack([
            dbc.Card([
                dbc.CardHeader("Input Text"),
                dbc.CardBody([
                    dbc.Textarea(
                        id="input-text-area",
                        value=lyrics.strip(),
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