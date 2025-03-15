# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""
import dash_bootstrap_components as dbc
import dash
from dash import html
from dbc_components import *

# Page layout for pg2
layout = html.Div([
    dbc.Breadcrumb(
        items=[{"label": page_names[idx], "href": page['path'], "active": idx == 1} for idx, page in enumerate(dash.page_registry.values())],
        class_name="navbar",
        ),
    dbc.Row([
        dbc.Col(hnp_card, width=12, sm=12, md=5,),
        dbc.Col(demo_card, width=12, sm=12, md=5,)
        
        ], class_name = "row_block_class", justify="evenly"),
])

# Register the page with a specific path
dash.register_page(__name__)

