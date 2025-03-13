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
    items=[
        {"label": page_names[idx], "href": page['path']}
        for idx, page in enumerate(dash.page_registry.values())
    ],
    class_name="navbar",
    
    ),
    # html.Div([dcc.Link(page['name']+" | ", href=page['path']) for page in dash.page_registry.values()]),

    dash.page_container
    ], class_name="container", fluid=True)


# @app.callback(
#     Output('hnp_text', 'children'),
#     Input('hnp_carousel', 'active_index')
# )
# def update_hnpcarousel_text(indeks):
#     if indeks:
#         return carousel_desc_list[indeks]
#     return carousel_desc_list[0]

@dash.callback(
    Output('hnp_text', 'children'),
    Input('hnp_carousel', 'active_index')
)
def update_hnpcarousel_text(indeks):
    if indeks:
        return carousel_desc_list[indeks]
    return carousel_desc_list[0]
# if __name__ == "__main__":
app.run_server(port=8050, host='0.0.0.0')

