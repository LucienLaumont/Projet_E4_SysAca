# Serveur central Flask
from flask import Flask
from model import generate_model,prediction_etudiant

from dash import Output,Input,State

server = Flask(__name__)

dropdown_options_E = [
    {'label': 'EL-3012', 'value': 'EL-3012'},
    {'label': 'EL-3013', 'value': 'EL-3013'},
    {'label': 'EL-3019', 'value': 'EL-3019'},
    {'label': 'EL-3020', 'value': 'EL-3020'},
    {'label': 'EL-3025', 'value': 'EL-3025'},
    {'label': 'EL-3031', 'value': 'EL-3031'},
    {'label': 'EL-3035', 'value': 'EL-3035'}
]

dropdown_options_F = [
    {'label': 'EL-3003', 'value': 'EL-3003'},
    {'label': 'EL-3005', 'value': 'EL-3005'},
    {'label': 'EL-3007', 'value': 'EL-3007'},
    {'label': 'EL-3017', 'value': 'EL-3017'},
    {'label': 'EL-3023', 'value': 'EL-3023'},
    {'label': 'EL-3027', 'value': 'EL-3027'},
    {'label': 'EL-3034', 'value': 'EL-3034'}
]

domaines =['Automotive','Environment','Construction','Tourism','Communication','Finance','Education','Energy','Farming','Telecom','Pharmaceutical','Media','Logistics','Aerospace']

entreprises = ['Thales', 'Orange', 'Siemens', 'Engie', 'Safran', 'Renault', 'Dassault systeme', 'BNP Paribas', 'Loreal', 'EQUANS']

# Première application Dash
from dash import Dash, html, dcc

app_front_page = Dash(server=server, routes_pathname_prefix='/')
app_front_page.layout = html.Div(className = 'wallpaper-rectangle',children = [
    dcc.Location(id='url', refresh=False),
    html.Div(className='title-rectangle', children=[
        html.H1("QUELLE EST TA FILIERE ?", className='title-mainpage')
    ]),
    html.Div(className='button-rectangle', id='my-button', children=[
        html.A("COMMENCE LE QUIZ !", href="/quiz/", className="button-mainpage")
    ])
])

# Seconde application Dash
app_quiz_page = Dash(server=server, routes_pathname_prefix='/quiz/')
app_quiz_page.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.H1("Trouve ta filière ! "),
    html.Div([
        html.Div([
            html.H3("Donne ton interêt pour chaque domaine : ", className= 'Titre_box'),
            *[html.Div([html.H3(domaine), dcc.Slider(id=f'{domaine}', min=1, max=5, step=1, value=3)], className='Domaines') for domaine in domaines]
        ], className='espace-entre-divs')
    ]),
 
    html.Div([
        html.Div([
            html.H3("Ouap_E",className= "Ouap"),
            dcc.Dropdown(
                id='dropdown_E',
                options=dropdown_options_E,
                value='EL-3012'
                
            ),
        ], className='espace-entre-divs')
    ]),
    
    html.Div([
        html.Div([
            html.H3("Ouap_F",className= "Ouap"),
            dcc.Dropdown(
                id='dropdown_F',
                options=dropdown_options_F,
                value='EL-3003'
            ),
        ], className='espace-entre-divs')
    ]),
    
    html.Div([
        html.H3("Donne ton interêt pour chaque entreprises",className= 'Titre_box'),
        *[html.Div([html.H3(entreprise), dcc.Slider(id=f'{entreprise}', min=1, max=5, step=1, value=3)], className='Entreprises') for entreprise in entreprises]
    ]),

    html.Div([
        html.Button('Résultat', id='submit-val', n_clicks=0, className='button-container'),
        html.Div(id='output-container-button', children='Voir les résultats', className='result-text')
    ])
], className='container')


app_resultat_page = Dash(server=server, routes_pathname_prefix='/resultat/')
app_resultat_page.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='result_image_container')  # Ce conteneur affichera l'image basée sur la prédiction
])

from dash import dcc, html, callback, callback_context
from dash.exceptions import PreventUpdate

@app_quiz_page.callback(
    Output('url', 'pathname'),
    [Input('submit-val', 'n_clicks')],
    [State(f'{entreprise}', 'value') for entreprise in entreprises] +
    [State(f'{domaine}', 'value') for domaine in domaines] +
    [State('dropdown_E', 'value'), State('dropdown_F', 'value')]
)
def redirect_to_result(n_clicks, *values):
    if n_clicks > 0:
        prediction = prediction_etudiant(values,domaines,entreprises,[option['value'] for option in dropdown_options_E + dropdown_options_F])
        prediction = model.predict(prediction)
        result_path = f"/resultat/?prediction={prediction}"
        return result_path
    else:
        raise PreventUpdate

import urllib.parse

@app_resultat_page.callback(
    Output('result_image_container', 'children'),  # Mettez à jour cet Output pour correspondre à l'ID du nouveau conteneur
    [Input('url', 'search')]
)
def display_result(search):
    query = urllib.parse.parse_qs(urllib.parse.urlparse(search).query)
    prediction = query.get('prediction', [''])[0]
    print(prediction)
    if prediction:
        # Construire le chemin vers l'image basée sur la prédiction
        image_src = f'/assets/{prediction}.jpg'
        # Retourner l'élément img pour être affiché dans le conteneur
        return html.Img(src=image_src, style={"width": "100%", "height": "auto"})
    return "Aucune prédiction fournie"

if __name__ == "__main__":
    model = generate_model()
    server.run(debug=True)
