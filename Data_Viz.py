import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (supposons que le fichier s'appelle "Data_Renamed.csv")
df = pd.read_csv("Data_Renamed.csv")

# Liste des domaines pour lesquels vous souhaitez générer des graphiques
selected_domains = ['Automotive', 'Environment', 'Construction', 'Tourism', 'Communication']

# Sélectionner les colonnes pertinentes
selected_columns = ['Field'] + [f'Interest_{domain}' for domain in selected_domains]

# Parcourir chaque domaine et chaque champ
for domain in selected_domains:
    for field in df['Field'].unique():
        field_data = df[df['Field'] == field]
        domain_counts = field_data[f'Interest_{domain}'].value_counts()
        
        # Créer un graphique à secteurs pour chaque domaine (field)
        fig, ax = plt.subplots()
        ax.pie(domain_counts, labels=[f"{i}" for i in domain_counts.index], autopct='%1.1f%%')
        ax.set_title(f"Interests of Students in Field: {field} - Domain: {domain}")
        plt.show()
