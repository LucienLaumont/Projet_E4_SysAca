import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_regression

# Fonction pour charger les données
def load_data():
    data = pd.read_csv("Data_Renamed.csv")
    data_cleaned = data.drop(['Timestamp', 'Email'], axis=1)

    # Sélection des colonnes spécifiques pour X
    interest_columns = ['Interest_Health','Interest_Automotive','Interest_Construction','Interest_Pharmaceutical','Interest_Media',
    'Interest_Logistics','Interest_Aerospace','Interest_Telecom','Interest_Tourism','Interest_Environment',
    'Interest_Finance','Interest_Education','Interest_Energy','Interest_Farming'
    ]
    
    tool_company_columns = [
        'Python', 'Matlab', 'R', 'linux', 'C/C++', 'java', 'wireshark', 'Excel',
        'Vivado', 'VHDL', 'PowerBI', 'Trnsys', 'Bash', 'Thalès', 'Orange', 'Siemens',
        'Engie', 'Safran', 'Renault', 'Dassault système', 'BNP Paribas', 'L\'Oréal',
        'EQUANS', 'C /C++'
    ]

    # Assemblage des caractéristiques X en excluant 'Field'
    X = data_cleaned[interest_columns + tool_company_columns]
    # Correction : 'C/C++' est listé deux fois, donc on le retire de la liste s'il y est en double
    X = X.drop(columns=['C /C++'], errors='ignore') if 'C /C++' in X.columns else X
    y = data["Field"]
    return X, y

# Fonction pour BSS
def bss(X, y):
    try:
        # Définir le nombre de features à sélectionner
        k = 7

        # Créer un objet SelectKBest
        selector = SelectKBest(f_regression, k=k)

        # Fit le model sur les données d'apprentissage
        selector.fit(X, y)

        # Obtenir les indices des features sélectionnées
        selected_indices = selector.get_support(indices=True)

        # Afficher les features sélectionnées
        print("Features sélectionnées:", X.columns[selected_indices])
    except ZeroDivisionError:
        print("Error: Target variable might have constant values or missing values. Please check your data.")

# Charger les données
X, y = load_data()

# Appliquer BSS
bss(X, y)