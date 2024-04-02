# app.py
import dash
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(className='wallpaper-rectangle', children=[
    html.Div(className='title-rectangle',children=[ 
        html.H1("QUELLE EST TA FILIERE ?",className='title-mainpage')
    ]),
    html.Div(className='button-rectangle',children=[
        html.H1("LANCER LE QUIZ !",className='button-mainpage')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
