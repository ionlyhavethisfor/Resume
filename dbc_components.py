# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:17:38 2025

@author: caspe
"""

import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash

page_names = ["Projects Overview", "Master's Thesis", "Democracy Visualized"]
breadcrumbs = dbc.Breadcrumb(
    items=[
        {"label": page_names[idx], "href": page['path']}
        for idx, page in enumerate(dash.page_registry.values())
    ],
    class_name="navbar",
    )

hnp_crumb = dbc.Breadcrumb(items=[
        {"label": "Video", "href": "#video"},
        {"label": "Gallery", "href": "#hnp"},
    ]),


hnp_carousel = dbc.Carousel(id='hnp_carousel',
    items=[
        {
            "key": "1",
            "src": "assets/hnp_portal.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "2",
            "src": "assets/mockup.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "3",
            "src": "assets/memorise_ad.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "4",
            "src": "assets/HNP_indiv_page.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "5",
            "src": "assets/HNP_colormap1.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "6",
            "src": "assets/HNP_wordcloud1.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "7",
            "src": "assets/HNP_countrybirthlib.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "8",
            "src": "assets/HNP_danishredcross.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "9",
            "src": "assets/HNP_dutch.png",
            "imgClassName": "carousel-img"
            },


    ],
    controls=True,
    indicators=True,
    variant='dark',
    class_name="carousel"
)

carousel_desc_list = [
    "HNP Portal in its default state",
    "The mock-up which was the basis for the project",
    "An early version of the HNP portal (together a mock-up and earlier student project) in a MEMORISE technical report",
    "Individual page selection",
    "Individual colored map with each location displayed as a glyph",
    "A word cloud, generated using text from individual testimonies",
    "Filtering using small selection of country of origin",
    "People liberated by the Danish Red Cross",
    "Filtering by interviews conducted in Dutch",
                      ]



demo_carousel = dbc.Carousel(id='demo_carousel',
    items=[
        {
            "key": "1",
            "src": "assets/democracy_intheworld.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "2",
            "src": "assets/westafrica_violence.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "3",
            "src": "assets/suffrage_kuwait_syria.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "4",
            "src": "assets/europe_freeandfair.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "5",
            "src": "assets/world_freeviolence.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "6",
            "src": "assets/world_domesticprop.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "7",
            "src": "assets/go_peru.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "8",
            "src": "assets/NA_propaganda.png",
            "imgClassName": "carousel-img"
            },
        {
            "key": "9",
            "src": "assets/africa_electedofficials.png",
            "imgClassName": "carousel-img"
            },
    ],
    controls=True,
    indicators=True,
    variant='dark',
    class_name="carousel"
)

demo_desc_list = [
    "Map color indicates current-year scores, while glyphs indicate future development",
    "Multiple countries can be selected, and some tabs give info about aggregates, best or worst, or individual country distributions",
    "Here we look at de jure suffrage for the Asia region. We see that there are still some countries that do not have suffrage",
    "Looking at free and fair elections in the Europe region",
    "Looking at world freedom from violence. We see that, since 2012, it has gone down hill in for instance Afghanistan and Venezuela",
    "Looking at world domestic propaganda since 2015. It is looking grim on that front!",
    "South America has no moved much in their respective democratic indices since 2000, except for Peru. Go Peru!",
    "Resurgence of domestic propaganda in the US",
    "Plummeting of legitimate (elected) rule in Africa, 2023",
                      ]




hnp_card = dbc.Card(
    [
        dbc.CardHeader(html.H1("Master's Thesis: HNP Portal")),
        dbc.CardImg(src="assets/hnp_portal.png", top=True),
        dbc.CardBody(
            [   html.H4("What is it?"),
                html.P(["An interactive dashboard developed as a prototype for the ",
                       html.A("MEMORISE", href="https://memorise.sdu.dk/", target="_blank"),
                       "  organization, part of the larger ",
                       html.A("Horizon Europe", href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en", target="_blank"),
                       " funding programme. It was the practical part of my master's thesis. ",
                       "'HNP' stands for 'Heritage of Nazi Persecution'."]),
                html.P(["This prototype is meant to serve as a portal for a dataset containing HNP materials. It uses the ", 
                        html.A("Visual History Archive", href='https://vha.usc.edu/home'), " dataset, which was made available to me. However, I am not allowed to publicize it."]),

                html.H4('Functionality?'),
                html.P(["It functions as a search engine and visualization tool for Heritage of Nazi Persecution material. "]),
                html.P('The left-hand side contains numerous filters that users can combine. The centre contains various visualizations that change depending on the filters, and the right-hand side allows users to select individual people for a closer look into their stories.')
            ]
        ),
    ],
)

demo_card = dbc.Card(
    [   
        dbc.CardHeader(html.H1("Democracy Visualized")),
        dbc.CardImg(src="assets/democracy_intheworld.png", top=True),
        dbc.CardBody(
            [   html.H4("What is it?"),
                html.P(["This was an exam probject for a data visualization class. It was supposed to be presented as a poster to the ",
                       html.A("EuroVis", href="https://event.sdu.dk/eurovis", target="_blank"),
                       " conference, but things got in the way. It was a group project, though I was in charge of the implementation due to experience with data visualization tools.",]),
                html.P(["It is a dashboard containing data from the ", 
                        html.A("V-Dem", href='https://v-dem.net/data/'), " dataset, which is publically available. ", 
                        "V-Dem gathers expert-sourced data from all over the world to measure democratic developments using a series of 'indices' that attempt to give a score to various aspects of a democratic society."]),

                html.H4('Functionality?'),
                html.P(["The dashboard allows users to select and compare individual countries, regions, or the world at various parts.",
                        " The map combines a classic choropleth color interval with glyphs indicating development over time. ", 
                        "Users can select individual years in the interval 2000-2024."]),
                html.P('')
            ])
    ],
)


