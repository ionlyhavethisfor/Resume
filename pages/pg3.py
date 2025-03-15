# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""

import dash_bootstrap_components as dbc
import dash
from dash import html
from dbc_components import *


bread = [
        {'label': page_names[0], 'href': '/'},
        {'label': page_names[1], 'href': '/pg2'},
        {'label': page_names[2], 'href': '/pg3', 'active': True},
        {'label': page_names[3], 'href': '/pg4'},]

# Page layout for pg3
layout = html.Div([
    dbc.Breadcrumb(
        items=bread,
        class_name="navbar",
        ),
    dbc.Tabs([
        dbc.Tab(
            dbc.Row([
                hnp_carousel, 
                html.P("", id="hnp_text")
            ], class_name="row_block_class", id="hnp"),
            
            label="Gallery", tab_id='gallery'),
        dbc.Tab(
            dbc.Row([
                html.Iframe(
                    src="https://www.youtube.com/embed/9tXKMm2DL68",
                    style={"width": "100%", "height": "auto", 'padding': '0 10vh 20vh 10vh'}
                ),
                ], class_name="row_block_class", id='video'),
            
            label="Video"),
    ], id="tabs", active_tab="gallery"),


])

# Register the page with a specific path
dash.register_page(__name__)


