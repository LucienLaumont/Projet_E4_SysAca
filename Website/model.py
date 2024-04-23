
from Etudiant_creator import generator_student

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def generate_model():

    #generator_student()
    data = pd.read_csv("etudiants.csv",sep=',')
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

    return model

def prediction_etudiant(quiz_responses, domaines, entreprises, cours):
    # Ordre des colonnes pour le DataFrame de prédiction
    columns_order = [        
        # Entreprises
        'Thales', 'Orange', 'Siemens', 'Engie', 'Safran', 
        'Renault', 'Dassault-systeme', 'BNP-Paribas', 'Loreal', 'EQUANS',

        # Domaines
        'Automotive', 'Environment', 'Construction', 'Tourism', 'Communication',
        'Finance', 'Education', 'Energy', 'Farming', 'Telecom',
        'Pharmaceutical', 'Media', 'Logistics', 'Aerospace',

        # Matières (Cours EL-XXXX pour E et F)
        'EL-3012', 'EL-3013', 'EL-3019', 'EL-3020', 'EL-3025', 
        'EL-3031', 'EL-3035','EL-3017','EL-3034','EL-3003','EL-3005','EL-3007', 
        'EL-3023', 'EL-3027',
    ]

    # Initialisation du dictionnaire pour stocker les valeurs des prédicteurs
    quiz_dict = {}
    
    # Gérer les réponses pour les domaines
    for i, domaine in enumerate(domaines):
        quiz_dict[domaine] = quiz_responses[i]
    
    # Gérer les réponses pour les cours
    # Supposons que les deux valeurs `str` pour les cours soient à la fin du tuple `quiz_responses`
    # Initialiser toutes les matières à 0
    for cours_code in cours:
        quiz_dict[cours_code] = 0
    
    # Mettre à jour les valeurs pour les cours sélectionnés
    selected_courses = quiz_responses[-2:]  # Prend les deux dernières valeurs du tuple pour les cours sélectionnés
    for cours_code in selected_courses:
        if cours_code in quiz_dict:
            quiz_dict[cours_code] = 1  # Marquer les cours sélectionnés avec 1
    
    # Gérer les réponses pour les entreprises
    # Supposons que les réponses pour les entreprises soient juste avant les matières sélectionnées
    # et juste après les domaines dans le tuple `quiz_responses`
    start_index_entreprises = len(domaines)  # L'index de début pour les réponses des entreprises dans quiz_responses
    end_index_entreprises = start_index_entreprises + len(entreprises)  # L'index de fin
    for i, entreprise in enumerate(entreprises):
        # Les valeurs pour les entreprises sont traitées comme binaires (intérêt: 1, pas d'intérêt: 0)
        quiz_dict[entreprise] = 1 if quiz_responses[start_index_entreprises + i] >= 3 else 0

    # Créer un DataFrame à partir du dictionnaire pour la prédiction

    return pd.DataFrame([quiz_dict], columns=columns_order)
    
    # Utiliser le modèle pour faire une prédiction basée sur df_for_prediction
    # predicted_filiere = model.predict(df_for_prediction)
    # print(f"Filière prédite : {predicted_filiere[0]}")
    