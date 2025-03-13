# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:17:38 2025

@author: caspe
"""

import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash

page_names = ["About Me", "Projects Overview", "HNP Portal", "Democracy Visualized"]
breadcrumbs = dbc.Breadcrumb(
    items=[
        {"label": page_names[idx], "href": page['path']}
        for idx, page in enumerate(dash.page_registry.values())
    ],
    class_name="navbar",
    
    )

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("Casper Louv Kamp", href="#"),
            dbc.Nav(
                [
                    dbc.NavLink("About", active=True, href="#"),
                    dbc.NavLink("Projects Overview", href="#"),
                    dbc.NavLink("HNP Portal", href="/hnp", external_link=True),
                    dbc.NavLink("Democracy Visualized", href="#"),
                ],
                className="ms-auto",  # Aligns nav items to the right
            ),
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
    className="navbar"
)


hnp_carousel = dbc.Carousel(id='hnp_carousel',
    items=[
        {
            "key": "1",
            "src": "assets/hnp_portal.png",
            },
        {
            "key": "2",
            "src": "assets/HNP_indiv_page.png",
            },
        {
            "key": "3",
            "src": "assets/HNP_danishredcross.png",
            },
        {
            "key": "4",
            "src": "assets/HNP_wordcloud1.png",
            },
        {
            "key": "5",
            "src": "assets/HNP_dutch.png",
            },
        {
            "key": "6",
            "src": "assets/HNP_colormap1.png",
            },
        {
            "key": "7",
            "src": "assets/HNP_countrybirthlib.png",
            },

    ],
    controls=True,
    indicators=True,
    variant='dark',
    class_name="carousel"
)

carousel_desc_list = ["HNP Portal in its default state", 
                      "Individual page selection", 
                      "People liberated by the Danish Red Cross",
                      "A word cloud, generated using text from individual testimonies",
                      "Filtering by interviews conducted in Dutch", 
                      "Individual colored map with each location displayed as a glyph",
                      "Filtering using small selection of country of origin"]


hnp_card = dbc.Card(
    [
        dbc.CardImg(src="assets/hnp_portal.png", top=True),
        dbc.CardHeader("Heritage of Nazi Persecution Portal"),
        dbc.CardBody(
            [   
                html.P(["Developed as a prototype for the ",
                       html.A("MEMORISE", href="https://memorise.sdu.dk/", target="_blank"),
                       "  organization, part of the larger ",
                       html.A("Horizon Europe", href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en", target="_blank"),
                       " funding programme."]),
                html.P("Functions as a search engine and visualization tool for Heritage of Nazi Persecution material. "
                       "Uses the Visual History Archive dataset as a test case."),
            ]
        ),
    ],
)

demo_card = dbc.Card(
    [
        dbc.CardImg(src="assets/democracy_intheworld.png", top=True),
        dbc.CardHeader("Democracy in the World"),
        dbc.CardBody(
            [
                html.P("Uses V-Dem dataset to visualize development of democratic indices over time."),
            ]
        ),
    ],
)



me_card = dbc.Card(
    [
        dbc.CardImg(src="assets/portrait-placeholder-Wide.png", top=True, className="img-fluid rounded-start"),
        dbc.CardBody(
            [
                html.H4("Casper Kamp", className="card-title"),
                html.P("Masters in Data Science"),
                html.P("Bachelors in American Studies"),
            ]
        ),
    ],
    style={"width": "18rem"},
)