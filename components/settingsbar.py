import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

def make_settings_bar(comp=[]):
    components = comp
    settings_header = dbc.Row(
        [
            dbc.Col(
                [
                    html.Button(
                        # use the Bootstrap navbar-toggler classes to style
                        html.Span(className="navbar-toggler-icon"),
                        className="navbar-toggler",
                        # the navbar-toggler classes don't set color
                        style={
                            "color": "rgba(0,0,0,.5)",
                            "border-color": "rgba(0,0,0,.1)",
                        },
                        id="settings-toggle",
                    ),
                ],
                # the column containing the toggle will be only as wide as the
                # toggle, resulting in the toggle being right aligned
                width="auto",
                # vertically align the toggle in the center
                align="center",
            ),
            dbc.Col(html.H2("Settings", className="display-4", id='settings-name')),

        ]
    )

    settings = html.Div(
        [settings_header,
         html.Div(
             [
                 html.Hr(),
                 components,
             ],
             id="settings-blurb",
         ),
         ],
        id="settings",
        className="collapsed",

    )

    return settings


@app.callback(
    Output("settings", "className"),
    [Input("settings-toggle", "n_clicks")],
    [State("settings", "className")],
)
def toggle_classname(n, classname):
    if n==None:
        return "collapsed"
    if n and classname == "":
        return "collapsed"
    return ""

