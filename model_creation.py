from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd

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


