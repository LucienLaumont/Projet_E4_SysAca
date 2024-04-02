
import pandas as pd

# Charger le fichier CSV
data = pd.read_csv('Data.csv')
from itertools import chain

# Définir les nouveaux noms de colonnes
new_column_names = {
    'Horodateur': 'Timestamp',
    'Adresse e-mail': 'Email',
    'Coche ta promo ': 'Promotion',
    'Coche ta filière si tu en as une ou celle que tu souhaites intégrer ': 'Field',
    'Ta filière est elle possible en alternance ? ': 'Alternance',
    'Ton intérêt pour le Médicale / La santé':                              'Interest_Health',
    "Ton intérêt pour l'automobile ":                                       'Interest_Automotive',
    'Ton intérêt pour le bâtiment / la construction ':                      'Interest_Construction',
    "Ton intérêt pour l'industrie pharmaceutique ":                         'Interest_Pharmaceutical',
    'Ton intérêt pour le divertissement et les médias':                     'Interest_Media',
    'Ton intérêt pour la logistique et le transport ':                      'Interest_Logistics',
    "Ton intérêt pour l'aéronautique et l'espace ":                         'Interest_Aerospace',
    "Ton intérêt pour la télécommunication ":                               'Interest_Telecom',
    "Ton intérêt pour le tourisme  " :                                      'Interest_Tourism',
    "Ton intérêt pour l'environnement  ":                                   'Interest_Environment',
    "Ton intérêt pour  les technologies de l'information et communication": 'Interest_Communication' ,
    "Ton intérêt pour la finance/banque ":                                  'Interest_Finance',
    "Ton intérêt pour l'éducation" :                                        'Interest_Education',
    "Ton intérêt pour l'énergie" :                                          'Interest_Energy',
    "Ton intérêt pour l'agriculture et l'agroalimentaire " :                'Interest_Farming',
    "Choisi les 3 langages de programmation / logiciel / système d'exploitation que tu préfères":               'Fav_Languages',
    'Coche 3 entreprises que tu souhaites intégrer ':                       'Preferred_Companies'
}

# Renommer les colonnes
data = data.rename(columns=new_column_names)

fav_languages = ["Python","Matlab","R","linux","C/C++","java","wireshark","Excel","Vivado","VHDL","PowerBI","Trnsys","Bash"]

fav_company =   ["Thalès","Orange","Siemens","Engie","Safran","Renault","Dassault système","BNP Paribas","L'Oréal","EQUANS"]



for languages in fav_languages:
       data[languages] = 0

for company in fav_company:
       data[company]   = 0

# Pour chaque individu, mettre à jour les colonnes correspondantes pour les entreprises et les langages de programmation
for i, row in data.iterrows():
    
    preferred_companies = [x.strip() for x in row['Preferred_Companies'].split(',')]
    fav_languages =       [x.strip() for x in row['Fav_Languages'].split(',')]

    # Mettre à jour pour les entreprise
    for company in preferred_companies:
            data.at[i, company] = 1

    # Mettre à jour pour les langages de programmation
    for language in fav_languages:
            data.at[i, language] = 1

data = data.drop(columns="Fav_Languages")
data = data.drop(columns="Preferred_Companies")

data.to_csv('Data_Renamed.csv', index=False)

