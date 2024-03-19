import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Chargement de votre jeu de données
data = pd.read_csv('Data_Renamed.csv')

data_cleaned = data.drop(['Timestamp', 'Email'], axis=1)

# Sélection des colonnes spécifiques pour X
interest_columns = [
    'Interest_Finance', 'Interest_Education', 'Interest_Energy',
    'Interest_Farming', 'Interest_Telecom', 'Interest_Pharmaceutical',
    'Interest_Media', 'Interest_Logistics', 'Interest_Aerospace'
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

# La variable cible y est 'Field'
y = data_cleaned['Field']

# Conversion de la variable cible en format numérique (nécessaire pour la régression logistique)
y_encoded = pd.factorize(y)[0]

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.25, random_state=42)

# Définition de la fonction pour calculer l'exactitude pour un ensemble de caractéristiques donné
def calculate_accuracy(features):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train[features], y_train)
    y_pred = model.predict(X_test[features])
    return accuracy_score(y_test, y_pred)


# Création de la liste de toutes les caractéristiques
all_features = list(X.columns)

# Initialisation des variables pour stocker les caractéristiques sélectionnées
selected_features = []
best_score = 0

# Boucle sur toutes les caractéristiques pour sélectionner la meilleure à chaque étape
while len(selected_features) < len(X.columns):
    best_feature = None
    best_feature_score = 0
    
    # Pour chaque caractéristique non encore sélectionnée, évaluez l'exactitude du modèle avec cette caractéristique ajoutée
    for feature in X.columns:
        if feature not in selected_features:
            score = calculate_accuracy(selected_features + [feature])
            if score > best_feature_score:
                best_feature = feature
                best_feature_score = score
    
    # Ajoutez la meilleure caractéristique à la liste sélectionnée et mettez à jour le meilleur score
    selected_features.append(best_feature)
    if best_feature_score > best_score:
        best_score = best_feature_score
    else:
        # Arrêtez la boucle si l'ajout de la meilleure caractéristique n'améliore pas le score
        break

print("Caractéristiques sélectionnées:", selected_features)
print("Exactitude correspondante:", best_score)


# Création de la liste de toutes les caractéristiques
all_features = list(X.columns)

# Initialisation des variables pour stocker les caractéristiques sélectionnées
selected_features = all_features
best_score = calculate_accuracy(selected_features)

# Boucle sur toutes les caractéristiques pour éliminer la moins importante à chaque étape
while len(selected_features) > 0:
    worst_feature = None
    worst_feature_score = best_score
    print("____________________________________________")
    print(best_score)
    # Pour chaque caractéristique sélectionnée, évaluez l'exactitude du modèle sans cette caractéristique
    for feature in selected_features:
        remaining_features = [f for f in selected_features if f != feature]
        score = calculate_accuracy(remaining_features)
        if score > worst_feature_score:
            worst_feature = feature
            worst_feature_score = score
    
    # Si la suppression de la moins importante améliore le score, mettez à jour les caractéristiques sélectionnées et le meilleur score
    print(worst_feature)
    if worst_feature is not None and worst_feature_score > best_score:
        selected_features = [f for f in selected_features if f != worst_feature]
        best_score = worst_feature_score
    else:
        # Arrêtez la boucle si aucune suppression n'améliore le score
        break

print("Caractéristiques sélectionnées:", selected_features)
print("Exactitude correspondante:", best_score)
