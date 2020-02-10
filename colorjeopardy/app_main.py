import dash
import dash_daq as daq
from flask import redirect
import dash_core_components as dcc
import dash_html_components as html
import sqlalchemy as db
import random
import datetime as dt
from .app import app

COLORS = [
    "pink",
    "colorless",
    "reddish brown",
    "purple",
    "brown",
    "red",
    "blue",
    "yellow",
    "green",
    "black",
    "violet",
    "rose",
    "deep blue",
    "sky blue",
    "pale yellow",
    "dark green",
    "red brown",
    "orange",
    "dark red",
    "grey",
    "white",
    "light blue",
    "black brown",
    "pale pink",
    "slightly pink",
    "red-brown",
    "light purple",
    "green yellow",
    "dark brown",
    "primrose yellow",
    "cyan",
    "light green",
    "faint pink",
    "orange brown",
    "dark blue",
    "red/purple",
    "blue green",
    "pale brown",
    "pink/purple",
    "light yellow",
    "pale green",
    "dark turquiose",
    "yellowish white",
    "light brown",
    "pale blue",
    "dark purple",
    "yellow-green",
    "black green",
    "green-yellow",
    "flavescens",
    "light pink",
    "intense violet",
    "aubergine",
    "yellowish yellow",
    "orange red",
    "deep-blue",
    "lilac",
    "pale violet",
    "courless",
    "dark-violet",
    "gold",
    "light red",
    "yellow-orange",
    "amber",
    "pale-yellow",
    "green-black",
    "buff",
    "deep yellow",
    "deep red",
    "whiteish colorless",
    "red-violet",
    "pale red",
    "lavender",
    "straw yellow",
    "yellow green",
    "brown-red",
    "purple black",
    "black purple",
    "turquoise",
    "brown orange",
    "light-purple",
    "greenish blue",
    "light violet",
    "aquamarine",
    "wheat",
    "ruby red",
    "navy blue",
    "deep purple",
    "green blue",
    "plate",
    "gray",
    "red-orange",
    "black-brown",
    "red purple",
    "dark pink",
    "dark purplish-red",
    "purple-red",
    "pink-violet",
    "blackish purple",
    "reddish purple",
    "bright yellow",
    "turquoise blue",
    "black red",
    "orange-red",
    "reddish",
    "greenish-yellow",
    "mauve",
    "orange-yellow",
    "dark violet",
    "red-yellow",
    "yellowish",
    "translucent",
    "magenta",
    "beige",
    "greenish cyan",
    "dark orange",
    "cherry red",
    "deep blue-black",
    "light orange",
    "deep brown",
    "green-blue",
    "dark yellow",
    "crimson",
    "orange yellow",
    "white",
    "claybank",
    "azure",
    "glaucous",
    "greenish green",
    "deep green",
    "violet red",
    "yellow-red",
    "greenish-blue",
    "light colorless",
    "brown yellow",
    "bluish violet",
    "golden yellow",
    "red-black",
    "intense purple",
    "peach",
    "scarlet",
    "dull dark black",
    "violet-red",
    "dark rose",
    "blue violet",
    "amaranthine",
    "jasmine",
    "light-brown",
    "purple-blue",
    "dark-blue",
    "pink-purple",
    "pink-red",
    "light",
    "purple red",
    "brown-yellow",
    "grass green",
    "jonquil",
    "yellowish green",
    "pale straw",
    "pale purple",
    "dark-red",
    "green/brown",
    "green-brown",
]



disk_engine = db.create_engine(
    "sqlite:///data_entry.db", connect_args={"check_same_thread": False}
)


connection = disk_engine.connect()
metadata = db.MetaData(connection)
SQL_table = db.Table(
    "data_entry",
    metadata,
    db.Column("color_string", db.String(255)),
    db.Column("hex", db.String(255)),
    db.Column("starttime", db.DATETIME),
    db.Column("time_stamp", db.DATETIME, primary_key=True),
)


COLOR = random.choice(COLORS)
r = lambda: random.randint(0, 255)
RAND_COLOR = "#%02X%02X%02X" % (r(), r(), r())
STARTTIME = dt.datetime.now()
COUNTER = 0
COUNTER_MAX = 5


def init_color():
    global COLOR
    global RAND_COLOR
    global STARTTIME
    COLOR = random.choice(COLORS)
    r = lambda: random.randint(0, 255)
    RAND_COLOR = "#%02X%02X%02X" % (r(), r(), r())
    STARTTIME = dt.datetime.now()



layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1(
                            "Please pick this color: {}".format(COLOR),
                            className="display-3",
                            id="h1",
                        ),
                        html.P(
                            "Help our research by selecting the color that most resembles the word using the color picker.",
                            className="lead",
                        ),
                        html.P(
                            "Use the top slider to select the color and bottom slider to select transparency and pointer for detailed selection.",
                            className="lead",
                        ),
                        daq.ColorPicker(
                            id="color-picker",
                            value=dict(hex=RAND_COLOR),
                            size=620,
                            theme={"dark": True, "detail": None, "secondary": None},
                            style={
                                "border": "0px solid",
                                "borderRadius": 0,
                                "outline": 0,
                                "boxShadow": None,
                                "textAlign": "Center",
                                "marginBottom": 20,
                                "width": "100%",
                                "display": "inline-block",
                            },
                        ),
                        html.Div(id="color-picker-output"),
                        html.Div(
                            [
                                html.P(
                                    "Click on 'Next' to save and get the next color.",
                                    className="lead",
                                )
                            ],
                            className="container",
                        ),
                        html.Button(
                            "Next ({}/{})".format(COUNTER, COUNTER_MAX),
                            id="next",
                            className="btn btn-primary btn-lg btn-block",
                        ),
                        html.Div(id="button-out", style={"display": "none"}),
                        html.P(),
                        html.Button(
                            "Skip",
                            id="skip",
                            className="btn btn-secondary btn-lg btn-block",
                        ),
                    ],
                    className="container",
                    id="main",
                ),
                html.Div(id="skip-button-out", style={"display": "none"}),
            ],
            className="jumbotron",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.H2("About"),
                        html.P(
                            "We will use this data to turn text descriptions of colors, that we often find in chemistry, into actual numbers. This will help us in building models that can predict the color of chemical compounds."
                        ),
                        html.P(
                            [
                                "If you want to learn more, feel free to contact ",
                                html.A("Kevin", href="mailto:kevin.jablonka@epfl.ch"),
                                ".",
                            ]
                        ),
                        html.P(
                            [
                                "We commit to relase this dataset in curated form under ",
                                html.A(
                                    "CC BY-SA 4.0 license",
                                    href="https://creativecommons.org/licenses/by-sa/4.0/",
                                ),
                                ".",
                            ]
                        ),
                        html.H2("Privacy"),
                        html.P("We will store no personal data that can identify you."),
                    ],
                    className="container",
                ),
                html.Hr(),
                html.Footer(
                    "© Laboratory of Molecular Simulation (LSMO), École polytechnique fédérale de Lausanne (EPFL)"
                ),
            ],
            className="container",
        ),
    ],
    # tag for iframe resizer
    **{"data-iframe-height": ""},
)

app.layout = layout

@app.callback(
    dash.dependencies.Output("h1", "children"),
    [dash.dependencies.Input("button-out", "children")],
)
def color_picker(color):
    return "Please pick this color: {}".format(COLOR)


@app.callback(
    dash.dependencies.Output("color-picker", "value"),
    [dash.dependencies.Input("button-out", "children")],
)
def color_picker(color):
    return dict(hex=RAND_COLOR)


@app.callback(
    dash.dependencies.Output("next", "children"),
    [dash.dependencies.Input("button-out", "children")],
)
def color_picker(color):
    return "Next ({}/{})".format(COUNTER, COUNTER_MAX)


@app.callback(
    dash.dependencies.Output("button-out", "children"),
    [
        dash.dependencies.Input("next", "n_clicks"),
        dash.dependencies.Input("skip", "n_clicks"),
    ],
    [dash.dependencies.State("color-picker", "value")],
)
def entry_to_db(submit_entry, skip, color):
    hexcolor = color["hex"]
    if submit_entry:
        time_stamp = dt.datetime.now()
        app.logger.info(
            "Logging to db. Color string: {}, hex: {}, starttime: {}. time_stamp: {}".format(
                COLOR, hexcolor, STARTTIME, time_stamp
            )
        )
        entry = [
            {
                "color_string": COLOR,
                "hex": hexcolor,
                "starttime": STARTTIME,
                "time_stamp": time_stamp,
            }
        ]
        insert_entry = connection.execute(db.insert(SQL_table), entry)
        init_color()
        global COUNTER
        COUNTER += 1
        if COUNTER >= COUNTER_MAX:
            app.logger.info(
                "Counter equals or exceeds max counter, forwarding to completion page."
            )
            redirect("/app_complete")
        # Forward to thank you when COUNTER == MAX_COUNTER
        return hexcolor
    if skip:
        app.logger.info("Skipping")
        init_color()
        hexcolor = color["hex"]
        return hexcolor

    raise dash.exceptions.PreventUpdate


@app.callback(
    dash.dependencies.Output("main", "style"),
    [dash.dependencies.Input("color-picker", "value")],
)
def update_output(value):
    return {"color": value["hex"]}