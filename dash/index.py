
from config import APP_PATH
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
# import pages for the app
from apps import home, page_table, page_results

server = app.server

# building the upper navigation bar
dropdown = dbc.Navbar(children=[
                dbc.NavItem(dbc.NavLink("About Performance", href="{}/home".format(APP_PATH), external_link=True)),
                dbc.NavItem(dbc.NavLink("|", active=False, disabled=True)),
                dbc.NavItem(dbc.NavLink("Results Tool", href="{}/page_results".format(APP_PATH), external_link=True)),
                dbc.NavItem(dbc.NavLink("|", active=False, disabled=True)),
                dbc.NavItem(dbc.NavLink("Data Table", href="{}/page_table".format(APP_PATH), external_link=True)),
               ],
               color="dark",
               dark=True,
               className="ml-1",
               style={'font-size':'1.5em'})

logo_bar = dbc.Container(
                        [
                         dbc.Row([
                                  dbc.Col(html.A([
                                          html.Img(src="{}/assets/IQT_Labs_Logo.png".format(APP_PATH),
                                                   style={
                                                          'height' : '100px',
                                                          'padding-top' : 10,
                                                          'padding-bottom' : 10,
                                                          'padding-left' : 30,
                                                         }
                                                  )
                                                 ], href='https://www.iqt.org/labs/'),
                                          width=4
                                         ),
                                  dbc.Col(
                                          html.A([
                                          html.Img(src="{}/assets/BNext_Logo.png".format(APP_PATH),
                                                   style={
                                                          'height' : '85px',
                                                          'padding-top' : 25,
                                                          'padding-bottom' : 0,
                                                         }
                                                  )
                                                 ], href='https://www.bnext.org/'),
                                          width=4
                                         ),
                                 ],
                                 justify="between")
                        ]
                       )

navbar = dbc.Navbar(

    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("COVID-19 Diagnostic Accuracy Tool", className="ml-1")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="{}/home".format(APP_PATH),
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    logo_bar,
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '{}/page_table'.format(APP_PATH):
        return page_table.layout
    elif pathname == '{}/page_results'.format(APP_PATH):
        return page_results.layout
    else:
        return home.layout

if __name__ == '__main__':
    #app.run_server(port=PORT, debug=False)
    app.run_server(host='127.0.0.1', debug=True)
