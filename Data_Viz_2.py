import pandas as pd

# Charger les données depuis un fichier CSV (supposons que le fichier s'appelle "Data_Renamed.csv")
df = pd.read_csv("Data_Renamed.csv")

# Liste des domaines pour lesquels vous souhaitez générer le tableau
selected_domains = ["Thalès","Orange","Siemens","Engie","Safran","Renault","Dassault système","BNP Paribas","L'Oréal","EQUANS"]

# Parcourir chaque filière
for field in df['Field'].unique():
    # Initialiser un dictionnaire pour stocker les pourcentages par domaine pour cette filière
    pourcentages_par_domaine = {}
    
    # Filtrer les données pour cette filière
    df_filiere = df[df['Field'] == field]
    
    # Calculer les pourcentages de chaque note pour chaque domaine d'intérêt
    for domain in selected_domains:
        domain_counts = df_filiere[f'{domain}'].value_counts(normalize=True) * 100
        pourcentages_par_domaine[domain] = domain_counts.round(1)
    
    # Créer un DataFrame à partir des pourcentages
    df_pourcentages = pd.DataFrame(pourcentages_par_domaine)
    
    # Remplacer les valeurs manquantes par 0 (si une note n'apparaît pas pour un domaine)
    df_pourcentages = df_pourcentages.fillna(0)
    
    # Enregistrer le DataFrame dans un fichier CSV
    df_pourcentages.to_csv(f"{field}_tableau.csv")
    
    print(f"Le tableau des pourcentages pour la filière {field} a été enregistré dans le fichier {field}_tableau.csv.")