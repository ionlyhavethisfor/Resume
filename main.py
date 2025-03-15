# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""

from dbc_components import *
from flask_caching import Cache
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, dcc, State, ctx, ALL, no_update, dash_table
import dash

color_mode_switch =  dbc.Stack([
    html.I(className="bi bi-brightness-high"),
    html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ])
    
    ], direction='horizontal', style={"position": "absolute", 'right': "5vw", 'top': "5vh"})

breadcrumb_pages = [{"label": page_names[idx], "href": page['path']} for idx, page in enumerate(dash.page_registry.values())]


# %%

app = Dash(__name__, use_pages=True, pages_folder='pages',
           external_stylesheets=[dbc.themes.JOURNAL, dbc.icons.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"},
           ],
           )
server = app.server
app.layout = dbc.Container([

    dbc.Breadcrumb(
        items=breadcrumb_pages,
        class_name="navbar",
        id="breadcrumb"
        ),
    color_mode_switch,

    dash.page_container
    ], class_name="container", fluid=True)
app.clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute("data-bs-theme", switchOn ? "light" : "dark"); 
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)

@dash.callback(
    Output('hnp_text', 'children'),
    Input('hnp_carousel', 'active_index')
)
def update_hnpcarousel_text(indeks):
    if indeks:
        return carousel_desc_list[indeks]
    return carousel_desc_list[0]


@dash.callback(
    Output('demo_text', 'children'),
    Input('demo_carousel', 'active_index')
)
def update_democarousel_text(indeks):
    if indeks:
        return demo_desc_list[indeks]
    return demo_desc_list[0]


# if __name__ == "__main__":
app.run_server(debug=False, use_reloader=False)

