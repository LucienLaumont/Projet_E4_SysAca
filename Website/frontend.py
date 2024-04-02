import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

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


app.layout = html.Div([
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

#### Pas fait : 
@app.callback(
    Output('output-container-button', 'children'),
    [Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('domaine', 'value'),
     dash.dependencies.State('ouap', 'value'),
     dash.dependencies.State('entreprise', 'value')])
def update_output(n_clicks, domaine, ouap, entreprise):
    if n_clicks > 0:
        return f'Vous avez cliqué {n_clicks} fois. Domaine: {domaine}, Ouap: {ouap}, Entreprise: {entreprise}'
    else:
        return 'Cliquez sur le bouton pour afficher les résultats'
######

if __name__ == '__main__':
    app.run_server(debug=True)
