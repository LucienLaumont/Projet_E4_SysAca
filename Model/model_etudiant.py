import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import KBinsDiscretizer
import matplotlib.pyplot as plt
import numpy as np 


data = pd.read_csv("etudiants_dsia.csv",sep=',')

best_params = {'max_depth': 20, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 300}

X = data.drop(columns=['Filiere'])
y = data['Filiere']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
# Initialiser et entraîner le modèle de forêt aléatoire
model = RandomForestClassifier(**best_params, random_state=42)
model.fit(X_train, y_train)

# Faire des prédictions sur l'ensemble de test
predictions = model.predict(X_test)

# Évaluer la performance du modèle
accuracy = accuracy_score(y_test, predictions)
print(f"Précision du modèle : {accuracy}")


