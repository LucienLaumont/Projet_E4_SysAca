import random

class Etudiant:
    def __init__(self, nom, prenom,filiere):
        self.nom                 = nom
        self.prenom              = prenom
        self.filiere             = filiere
        self.domaine_interets    = {"Environnement": 0,"Automobile": 0,"Finance": 0,"Sante": 0}
        self.niveau_outils       = {"Matlab" : 0,"Python": 0,"C": 0,"Microcontrolleur": 0,"VHDL": 0,"Microprocesseur": 0,"Electronique": 0,"Probabilite": 0,"Reseau": 0,"IA": 0}
        self.interet_entreprises = {"Google" : 0,"Microsoft" : 0,"IBM" : 0,"Dassault" : 0,"Thales" : 0,"Airbus" : 0,"Total" : 0,"Capgemini" : 0,"Sanofi" : 0,"Vinci" : 0,"Orange" : 0,"Renault" : 0,"Nestlé" : 0,"Samsung" : 0}

    def create_student(self):
        method_name = f"student_{self.filiere}"
        if hasattr(self, method_name):
            return getattr(self, method_name)()
        else:
            return self.student_default()


    def student_DSIA(self):
        self.niveau_outils["Matlab"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0, 0.5, 0.3, 0.4, 0.4, 0.3])[0]
        self.niveau_outils["Python"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0.65, 0.25, 0.05, 0.03, 0.02,0])[0]
        self.niveau_outils["C"]                = random.choices([5, 4, 3, 2, 1, 0], weights=[0.15, 0.15, 0.30, 0.15, 0.10, 0.05])[0]
        self.niveau_outils["Microcontrolleur"] = random.choices([5, 4, 3, 2, 1, 0], weights=[0., 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["VHDL"]             = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Microprocesseur"]  = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Electronique"]     = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Probabilite"]      = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Reseau"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0.05, 0.10, 0.15, 0.3, 0.3, 0.3])[0]
        self.niveau_outils["IA"]               = random.choices([5, 4, 3, 2, 1, 0], weights=[0.7, 0.15, 0.5, 0.5, 0.5, 0])[0]
        
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.2, 0.345, 0.236, 0.091, 0.127])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.127, 0.073, 0.473, 0.182, 0.145])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.455, 0.273, 0.255, 0.018, 0.0])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.364, 0.309, 0.073, 0.145, 0.109])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.055, 0.091, 0.345, 0.273, 0.236])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.091, 0.145, 0.236, 0.273, 0.255])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.127, 0.2, 0.309, 0.255, 0.109])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.273, 0.218, 0.327, 0.145, 0.036])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.382, 0.236, 0.273, 0.109, 0.0])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.218, 0.4, 0.2, 0.127, 0.055])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.382, 0.255, 0.2, 0.145, 0.018])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.018, 0.2, 0.273, 0.364, 0.145])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.236, 0.255, 0.291, 0.164, 0.055])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.073, 0.145, 0.273, 0.218, 0.291])[0]


    def student_AIC(self):
        # Logique pour créer un étudiant en AIC
        self.domaine_interets["Matlab"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0, 0.5, 0.3, 0.4, 0.4, 0.3])[0]
        self.domaine_interets["Python"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0.65, 0.25, 0.05, 0.03, 0.02,0])[0]
        self.domaine_interets["C"]                = random.choices([5, 4, 3, 2, 1, 0], weights=[0.15, 0.15, 0.30, 0.15, 0.10, 0.05])[0]
        self.domaine_interets["Microcontrolleur"] = random.choices([5, 4, 3, 2, 1, 0], weights=[0., 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.domaine_interets["VHDL"]             = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.domaine_interets["Microprocesseur"]  = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.domaine_interets["Electronique"]     = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.domaine_interets["Probabilite"]      = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.domaine_interets["Reseau"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0.05, 0.10, 0.15, 0.3, 0.3, 0.3])[0]
        self.domaine_interets["IA"]               = random.choices([5, 4, 3, 2, 1, 0], weights=[0.7, 0.15, 0.5, 0.5, 0.5, 0])[0]
        
        self.interet_entreprises = {
            "Thales": random.choices([1, 0], weights=[0.895, 0.105])[0],
            "Orange": random.choices([1, 0], weights=[0.368, 0.632])[0],
            "Siemens": random.choices([1, 0], weights=[0.053, 0.947])[0],
            "Engie": random.choices([1, 0], weights=[0.053, 0.947])[0],
            "Safran": random.choices([1, 0], weights=[0.526, 0.474])[0],
            "Renault": random.choices([1, 0], weights=[0.263, 0.737])[0],
            "Dassault systeme": random.choices([1, 0], weights=[0.579, 0.421])[0],
            "BNP Paribas": random.choices([1, 0], weights=[0.421, 0.579])[0],
            "L'Oreal": random.choices([1, 0], weights=[0.105, 0.895])[0],
            "EQUANS": random.choices([1, 0], weights=[0, 0.1])[0]
        }
        
    def student_CYB(self):
        # Logique pour créer un étudiant en CYB
        self.niveau_outils["Matlab"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0, 0.5, 0.3, 0.4, 0.4, 0.3])[0]
        self.niveau_outils["Python"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0.65, 0.25, 0.05, 0.03, 0.02,0])[0]
        self.niveau_outils["C"]                = random.choices([5, 4, 3, 2, 1, 0], weights=[0.15, 0.15, 0.30, 0.15, 0.10, 0.05])[0]
        self.niveau_outils["Microcontrolleur"] = random.choices([5, 4, 3, 2, 1, 0], weights=[0., 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["VHDL"]             = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Microprocesseur"]  = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Electronique"]     = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Probabilite"]      = random.choices([5, 4, 3, 2, 1, 0], weights=[0.6, 0.3, 0.05, 0.025, 0.015, 0.01])[0]
        self.niveau_outils["Reseau"]           = random.choices([5, 4, 3, 2, 1, 0], weights=[0.05, 0.10, 0.15, 0.3, 0.3, 0.3])[0]
        self.niveau_outils["IA"]               = random.choices([5, 4, 3, 2, 1, 0], weights=[0.7, 0.15, 0.5, 0.5, 0.5, 0])[0]

        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.109, 0.217, 0.326, 0.217, 0.130])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.304, 0.370, 0.239, 0.087, 0.000])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.457, 0.087, 0.261, 0.130, 0.065])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.065, 0.065, 0.130, 0.283, 0.457])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.152, 0.130, 0.217, 0.326, 0.174])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.152, 0.152, 0.217, 0.326, 0.152])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.239, 0.239, 0.283, 0.174, 0.065])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.457, 0.217, 0.174, 0.109, 0.043])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.152, 0.130, 0.174, 0.435, 0.109])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.304, 0.326, 0.261, 0.065, 0.043])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.043, 0.152, 0.261, 0.370, 0.174])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.261, 0.196, 0.283, 0.196, 0.065])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.065, 0.130, 0.261, 0.304, 0.239])[0]
                
         self.interet_entreprises = {
            "Thales": random.choices([1, 0], weights=[0.804, 0.196])[0],
            "Orange": random.choices([1, 0], weights=[0.609, 0.391])[0],
            "Siemens": random.choices([1, 0], weights=[0.196, 0.804])[0],
            "Engie": random.choices([1, 0], weights=[0.13, 0.87])[0],
            "Safran": random.choices([1, 0], weights=[0.283, 0.717])[0],
            "Renault": random.choices([1, 0], weights=[0.196, 0.804])[0],
            "Dassault systeme": random.choices([1, 0], weights=[0.5, 0.5])[0],
            "BNP Paribas": random.choices([1, 0], weights=[0.348, 0.652])[0],
            "L'Oreal": random.choices([1, 0], weights=[0.13, 0.87])[0],
            "EQUANS": random.choices([1, 0], weights=[0.109, 0.891])[0]
        }
        
        
    def student_GI(self):
        self.domaine_interets["Automotive"]      = random.choices([1,2,3,4,5], weights=[0.114 ,0.114,0.171 ,0.343,0.257])[0]
        self.domaine_interets["Environnement"]    = random.choices([1,2,3,4,5], weights=[0.057 ,0.200,0.286,0.343,0.114])[0]
        self.domaine_interets["Construction"]     = random.choices([1,2,3,4,5], weights=[0.200,0.143,0.400,0.229,0.029])[0]
        self.domaine_interets["Tourism"]          = random.choices([1,2,3,4,5], weights=[0.343,0.229,0.171,0.114,0.143])[0]
        self.domaine_interets["Communication"]    = random.choices([1,2,3,4,5], weights=[0.114,0.257,0.286,0.286,0.057])[0]
        self.domaine_interets["Finance"]          = random.choices([1,2,3,4,5], weights=[0.200,0.343,0.029,0.257,0.171])[0]
        self.domaine_interets["Education"]        = random.choices([1,2,3,4,5], weights=[0.114,0.171,0.343,0.229,0.143])[0]
        self.domaine_interets["Energy"]           = random.choices([1,2,3,4,5], weights=[0.143,0.286,0.286,0.171,0.114])[0]
        self.domaine_interets["Farming"]          = random.choices([1,2,3,4,5], weights=[0.257,0.371,0.229,0.057,0.086])[0]
        self.domaine_interets["Telecom"]          = random.choices([1,2,3,4,5], weights=[0.4,0.343,0.143,0.114,0.00001])[0]
        self.domaine_interets["Pharmaceutical"]   = random.choices([1,2,3,4,5], weights=[0.229,0.371,0.229,0.114,0.057])[0]
        self.domaine_interets["Media"]            = random.choices([1,2,3,4,5], weights=[0.229,0.371,0.229,0.114,0.057])[0]
        self.domaine_interets["Logistics"]        = random.choices([1,2,3,4,5], weights=[0.0,0.171,0.143,0.2,0.486])[0]
        self.domaine_interets["Aerospace"]        = random.choices([1,2,3,4,5], weights=[0.0,0.143,0.171,0.286,0.4])[0]

        self.interet_entreprises["Thales"] = random.choices([0,1], weights=[0.486, 0.514])[0]
        self.interet_entreprises["Orange"] = random.choices([0,1], weights=[0.914, 0.086])[0]
        self.interet_entreprises["Siemens"] = random.choices([0,1], weights=[0.943, 0.057])[0]
        self.interet_entreprises["Engie"] = random.choices([0,1], weights=[0.914, 0.086])[0]
        self.interet_entreprises["Safran"] = random.choices([0,1], weights=[0.314, 0.686])[0]
        self.interet_entreprises["Renault"] = random.choices([0,1], weights=[0.514, 0.486])[0]
        self.interet_entreprises["Dassault_systeme"] = random.choices([0,1], weights=[0.429, 0.571])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0,1], weights=[1, 0])[0]
        self.interet_entreprises["L'Oreal"] = random.choices([0,1], weights=[0.543, 0.457])[0]
        self.interet_entreprises["Equans"] = random.choices([0,1], weights=[0.914, 0.086])[0]


    def student_SE(self):
        # Logique pour créer un étudiant en SE
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.071, 0.107, 0.286, 0.250, 0.286])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.089, 0.286, 0.357, 0.179, 0.089])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.357, 0.357, 0.196, 0.071, 0.018])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.518, 0.232, 0.143, 0.071, 0.036])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.054, 0.250, 0.375, 0.071, 0.250])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.339, 0.250, 0.268, 0.071, 0.071])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.268, 0.304, 0.232, 0.161, 0.036])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.143, 0.375, 0.214, 0.232, 0.036])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.482, 0.232, 0.196, 0.054, 0.036])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.179, 0.393, 0.250, 0.125, 0.054])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.518, 0.250, 0.125, 0.089, 0.018])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.179, 0.161, 0.339, 0.161, 0.161])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.179, 0.143, 0.214, 0.268, 0.196])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.054, 0.054, 0.107, 0.125, 0.661])[0]

        self.interet_entreprises["Thales"] = random.choices([0,1], weights=[0.286, 0.714])[0]
        self.interet_entreprises["Orange"] = random.choices([0,1], weights=[0.929, 0.071])[0]
        self.interet_entreprises["Siemens"] = random.choices([0,1], weights=[0.661, 0.339])[0]
        self.interet_entreprises["Engie"] = random.choices([0,1], weights=[0.964, 0.036])[0]
        self.interet_entreprises["Safran"] = random.choices([0,1], weights=[0.232, 0.768])[0]
        self.interet_entreprises["Renault"] = random.choices([0,1], weights=[0.643, 0.357])[0]
        self.interet_entreprises["Dassault_systeme"] = random.choices([0,1], weights=[0.357, 0.643])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0,1], weights=[0.946, 0.054])[0]
        self.interet_entreprises["L'Oreal"] = random.choices([0,1], weights=[0.929, 0.071])[0]
        self.interet_entreprises["Equans"] = random.choices([0,1], weights=[1, 0])[0]


    def student_SEI(self):
        # Logique pour créer un étudiant en SEI
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.0, 0.267, 0.2, 0.267, 0.267])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.0, 0.267, 0.4, 0.067, 0.267])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.333, 0.2, 0.333, 0.133, 0.0])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.333, 0.267, 0.267, 0.133, 0.0])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.0, 0.0, 0.4, 0.4, 0.2])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.133, 0.2, 0.4, 0.2, 0.067])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.2, 0.0, 0.4, 0.267, 0.133])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.067, 0.2, 0.467, 0.2, 0.067])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.333, 0.267, 0.333, 0.067, 0.0])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.067, 0.067, 0.4, 0.4, 0.067])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.267, 0.4, 0.267, 0.067, 0.0])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.133, 0.067, 0.4, 0.133, 0.267])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.133, 0.2, 0.2, 0.267, 0.2])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.0, 0.067, 0.333, 0.133, 0.467])[0]

        self.interet_entreprises["Thales"] = random.choices([1, 0], weights=[0.2, 0.8])[0]
        self.interet_entreprises["Orange"] = random.choices([1, 0], weights=[0.933, 0.067])[0]
        self.interet_entreprises["Siemens"] = random.choices([1, 0], weights=[0.933, 0.067])[0]
        self.interet_entreprises["Engie"] = random.choices([1, 0], weights=[1.0, 0.0])[0]
        self.interet_entreprises["Safran"] = random.choices([1, 0], weights=[0.267, 0.733])[0]
        self.interet_entreprises["Renault"] = random.choices([1, 0], weights=[0.467, 0.533])[0]
        self.interet_entreprises["Dassault systeme"] = random.choices([1, 0], weights=[0.6, 0.4])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([1, 0], weights=[1.0, 0.0])[0]
        self.interet_entreprises["L'Oreal"] = random.choices([1, 0], weights=[0.8, 0.2])[0]
        self.interet_entreprises["EQUANS"] = random.choices([1, 0], weights=[1.0, 0.0])[0]


    def student_ENE(self):
        # Logique pour créer un étudiant en ENE
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.258, 0.258, 0.258, 0.161, 0.065])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.000, 0.000, 0.161, 0.323, 0.516])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.097, 0.129, 0.161, 0.355, 0.258])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.355, 0.194, 0.161, 0.161, 0.129])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.129, 0.194, 0.419, 0.194, 0.065])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.290, 0.258, 0.226, 0.194, 0.032])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.129, 0.226, 0.226, 0.323, 0.097])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.000, 0.032, 0.000, 0.065, 0.903])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.129, 0.355, 0.129, 0.323, 0.065])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.194, 0.452, 0.290, 0.032, 0.032])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.323, 0.355, 0.258, 0.065, 0.000])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.258, 0.161, 0.194, 0.226, 0.161])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.258, 0.129, 0.387, 0.161, 0.065])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.129, 0.129, 0.226, 0.226, 0.290])[0]

        self.interet_entreprises["Thales"] = random.choices([0, 1], weights=[0.548, 0.452])[0]
        self.interet_entreprises["Orange"] = random.choices([0, 1], weights=[0.935, 0.065])[0]
        self.interet_entreprises["Siemens"] = random.choices([0, 1], weights=[0.742, 0.258])[0]
        self.interet_entreprises["Engie"] = random.choices([0, 1], weights=[0.129, 0.871])[0]
        self.interet_entreprises["Safran"] = random.choices([0, 1], weights=[0.677, 0.323])[0]
        self.interet_entreprises["Renault"] = random.choices([0, 1], weights=[0.742, 0.258])[0]
        self.interet_entreprises["Dassault Systeme"] = random.choices([0, 1], weights=[0.710, 0.290])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0, 1], weights=[0.839, 0.161])[0]
        self.interet_entreprises["LOreal"] = random.choices([0, 1], weights=[0.935, 0.065])[0]
        self.interet_entreprises["EQUANS"] = random.choices([0, 1], weights=[0.613, 0.387])[0]


    
    def student_BIO(self):
        # Logique pour créer un étudiant en BIO
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.542, 0.208, 0.083, 0.125, 0.042])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.125, 0.167, 0.375, 0.208, 0.125])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.625, 0.083, 0.208, 0.042, 0.042])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.375, 0.250, 0.208, 0.083, 0.083])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.167, 0.167, 0.500, 0.125, 0.042])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.375, 0.208, 0.208, 0.125, 0.083])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.125, 0.167, 0.417, 0.250, 0.042])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.208, 0.208, 0.458, 0.042, 0.083])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.417, 0.167, 0.292, 0.083, 0.042])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.292, 0.500, 0.167, 0.042, 0.000])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.042, 0.083, 0.167, 0.375, 0.333])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.292, 0.167, 0.292, 0.250, 0.000])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.333, 0.458, 0.208, 0.000, 0.000])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.333, 0.292, 0.208, 0.083, 0.083])[0]

        self.interet_entreprises["Thales"] = random.choices([1, 0], weights=[0.458, 0.542])[0]
        self.interet_entreprises["Orange"] = random.choices([1, 0], weights=[0.708, 0.292])[0]
        self.interet_entreprises["Siemens"] = random.choices([1, 0], weights=[0.792, 0.208])[0]
        self.interet_entreprises["Engie"] = random.choices([1, 0], weights=[0.792, 0.208])[0]
        self.interet_entreprises["Safran"] = random.choices([1, 0], weights=[0.667, 0.333])[0]
        self.interet_entreprises["Renault"] = random.choices([1, 0], weights=[0.958, 0.042])[0]
        self.interet_entreprises["Dassault systeme"] = random.choices([1, 0], weights=[0.708, 0.292])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([1, 0], weights=[0.917, 0.083])[0]
        self.interet_entreprises["L'Oreal"] = random.choices([1, 0], weights=[0.292, 0.708])[0]
        self.interet_entreprises["EQUANS"] = random.choices([1, 0], weights=[1.0, 0.0])[0]


    def student_INF(self):
        # Logique pour créer un étudiant en INF
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.243, 0.135, 0.243, 0.243, 0.135])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.297, 0.189, 0.405, 0.108, 0.000])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.378, 0.297, 0.216, 0.108, 0.000])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.405, 0.270, 0.162, 0.108, 0.054])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.027, 0.081, 0.162, 0.459, 0.270])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.243, 0.081, 0.378, 0.162, 0.135])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.162, 0.162, 0.432, 0.135, 0.108])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.297, 0.216, 0.351, 0.108, 0.027])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.514, 0.270, 0.189, 0.027, 0.000])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.216, 0.189, 0.351, 0.216, 0.027])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.432, 0.243, 0.189, 0.081, 0.054])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.054, 0.135, 0.270, 0.270, 0.270])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.189, 0.270, 0.459, 0.081, 0.000])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.135, 0.108, 0.297, 0.297, 0.162])[0]
        
        self.interet_entreprises["Thales"] = random.choices([0, 1], weights=[0.432, 0.568])[0]
        self.interet_entreprises["Orange"] = random.choices([0, 1], weights=[0.622, 0.378])[0]
        self.interet_entreprises["Siemens"] = random.choices([0, 1], weights=[0.892, 0.108])[0]
        self.interet_entreprises["Engie"] = random.choices([0, 1], weights=[0.946, 0.054])[0]
        self.interet_entreprises["Safran"] = random.choices([0, 1], weights=[0.703, 0.297])[0]
        self.interet_entreprises["Renault"] = random.choices([0, 1], weights=[0.622, 0.378])[0]
        self.interet_entreprises["Dassault Systeme"] = random.choices([0, 1], weights=[0.514, 0.486])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0, 1], weights=[0.622, 0.378])[0]
        self.interet_entreprises["LOreal"] = random.choices([0, 1], weights=[0.919, 0.081])[0]
        self.interet_entreprises["EQUANS"] = random.choices([0, 1], weights=[1.000, 0.000])[0]

        


    def student_default(self):
        # Logique pour créer un étudiant par défaut
        pass


# Exemple d'utilisation :
etudiant1 = Etudiant("Dupont", "Jean")
etudiant1.definir_filiere()
etudiant1.remplir_aleatoirement()
print("Nom:", etudiant1.nom)
print("Prénom:", etudiant1.prenom)
print("Filière:", etudiant1.filiere)
print("Domaines d'intérêt:", etudiant1.domaine_interets)
print("Niveau d'outils:", etudiant1.niveau_outils)
print("Intérêt pour les entreprises:", etudiant1.interet_entreprises)
