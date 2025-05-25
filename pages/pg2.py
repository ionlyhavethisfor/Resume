# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""
import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
from dbc_components import *

dash.register_page(__name__, path="/")

bread = [
        {'label': page_names[0], 'href': '/', 'active': True},
        {'label': page_names[1], 'href': '/thesis'},
        {'label': page_names[2], 'href': '/democracy'}]

# Page layout for pg1
layout = html.Div([
    dbc.Breadcrumb(
        items=bread,
        class_name="navbar",
        ),
    dbc.Row([
        dbc.Col(hnp_card, width=12, sm=12, md=5,),
        dbc.Col(demo_card, width=12, sm=12, md=5,)
        
        ], class_name = "row_block_class", justify="evenly"),
])


# Register the page with a specific path


