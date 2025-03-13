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
    dbc.Row([
        hnp_carousel, 
        html.P("", id="hnp_text")
    ], class_name="row_block_class", id="hnp"),
])

# Register the page with a specific path
dash.register_page(__name__)


