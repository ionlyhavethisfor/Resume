# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:13:21 2025

@author: caspe
"""

import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
from dbc_components import *

# Page layout for pg1
layout = dbc.Container([
    html.H1("Casper Louv Kamp", style={'width': "100vw"}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H2("Who am I?"),
            html.Ul([
                html.Li(["I am a new Data Science graduate from the ", 
                    html.A("University of Southern Denmark", href="https://www.sdu.dk/en", target="blank"),
                    ". My BA was in American Studies, also at SDU"
                ]),
                html.Li("I enjoyed working with data visualization, particularly creating interactive dashboards"),
                html.Li(["I am a ",
                        html.A("fairly good chess player", href="https://ratings.fide.com/profile/1470230", target="blank"),
                        ", albeit not very active"]),
            ])
            ], width=3, class_name='list'),
        
        dbc.Col([
            html.H2("What are my skills?"),
            html.Ul([
                html.Li("Data Visualization, particularly with Plotly"),
                html.Li("Web Development: Mainly using the Dash framework (and of course HTML, CSS)"),
                html.Li("Programming Languages: Python, some R"),
                html.Li("DBM: Practical experience with SQL as part of my thesis"),
            ])
            ], width=3, class_name='list'),
        
        dbc.Col([
            html.H2("What is this page?"),
            html.Ul([
                html.Li("This is my resumé website"),
                html.Li("It contains some information about me, as well as projects I have worked on that I feel are worth sharing"),
                html.Li(["I built this page using ", 
                        html.A("Dash", href="https://dash.plotly.com/r", target='blank'), " in combination with ",
                        html.A("Dash Bootstrap Components", href="https://dash-bootstrap-components.opensource.faculty.ai/", target='blank')]),
            ])
            ], width=3, class_name='list'),
        ], class_name = "row_block_class", justify="around"),
], class_name="container", fluid=True)

# Register the page with a specific path
dash.register_page(__name__, path="/")

