import dash_html_components as html
import dash_bootstrap_components as dbc
from components.settingsbar import make_settings_bar

layout = [html.Div("This is the Simple Drawer Page!"),make_settings_bar()]