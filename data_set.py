
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
    'Ton intérêt pour le Médicale / La santé': 'Interest_Health',
    "Ton intérêt pour l'automobile ": 'Interest_Automotive',
    'Ton intérêt pour le bâtiment / la construction ': 'Interest_Construction',
    "Ton intérêt pour l'industrie pharmaceutique ": 'Interest_Pharmaceutical',
    'Ton intérêt pour le divertissement et les médias': 'Interest_Media',
    'Ton intérêt pour la logistique et le transport ': 'Interest_Logistics',
    "Ton intérêt pour l'aéronautique et l'espace ": 'Interest_Aerospace',
    'Choisi les 3 langages de programmation que tu préfères': 'Fav_Languages',
    'Coche 3 entreprises que tu souhaites intégrer ': 'Preferred_Companies'
}

# Renommer les colonnes
data = data.rename(columns=new_column_names)

columns_to_drop = [col for col in data.columns if col.startswith('Ton intérêt')]

# Supprimer ces colonnes du DataFrame
data = data.drop(columns=columns_to_drop)

lst_language = []
lst_companie = []

for Languages in data['Fav_Languages'] : 
    mots_separes = Languages.split(', ')
    for mot in mots_separes:
        if mot not in lst_language:
            lst_language.append(mot)

for Companie in data['Preferred_Companies'] : 
    mots_separes = Companie.split(', ')
    for mot in mots_separes:
        if mot not in lst_companie:
            lst_companie.append(mot)

print(lst_language)
print(lst_companie)

for nom in lst_language:
    data[nom] = 0 


for nom in lst_companie:
    data[nom] = 0 

# Pour chaque individu, mettre à jour les colonnes correspondantes pour les entreprises et les langages de programmation
for i, row in data.iterrows():
    # Simuler la lecture des préférences depuis les exemples fournis
    preferred_companies = [x.strip() for x in row['Preferred_Companies'].split(',')]
    fav_languages = [x.strip() for x in row['Fav_Languages'].split(',')]

    # Mettre à jour pour les entreprises
    for company in preferred_companies:
            data.at[i, company] = 1

    # Mettre à jour pour les langages de programmation
    for language in fav_languages:
            data.at[i, language] = 1

data = data.drop(columns="Fav_Languages")
data = data.drop(columns="Preferred_Companies")

data.to_csv('Data_Renamed.csv', index=False)

