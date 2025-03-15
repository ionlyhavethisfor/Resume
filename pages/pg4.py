# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""

import dash_bootstrap_components as dbc
import dash
from dash import html
from dbc_components import *

# Page layout for pg4
layout = html.Div([
    dbc.Breadcrumb(
        items=[{"label": page_names[idx], "href": page['path'], "active": idx == 3} for idx, page in enumerate(dash.page_registry.values())],
        class_name="navbar",
        ),
    dbc.Tabs([
        dbc.Tab(
            dbc.Row([
                demo_carousel, 
                html.P("", id="demo_text")
            ], class_name="row_block_class", id="hnp"),
            label="Gallery", tab_id='gallery'
            ),
        dbc.Tab(html.H2('Working demo coming eventually..'), label="Demo")
        
        ], active_tab='gallery')

])

# Register the page with a specific path
dash.register_page(__name__)


