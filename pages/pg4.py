# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""

import dash_bootstrap_components as dbc
import dash
from dash import html
from dbc_components import *

dash.register_page(__name__)


bread = [
        {'label': page_names[0], 'href': '/'},
        {'label': page_names[1], 'href': '/pg3'},
        {'label': page_names[2], 'href': '/pg4', 'active': True},]

# Page layout for pg4
layout = html.Div([
    dbc.Breadcrumb(
        items=bread,
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





