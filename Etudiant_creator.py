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

    def student_AIC(self):
        # Logique pour créer un étudiant en AIC
        pass

    def student_CYB(self):
        # Logique pour créer un étudiant en CYB
        pass

    def student_GI(self):
        # Logique pour créer un étudiant en GI
        pass

    def student_SE(self):
        # Logique pour créer un étudiant en SE
        pass

    def student_SEI(self):
        # Logique pour créer un étudiant en SEI
        pass

    def student_ENE(self):
        # Logique pour créer un étudiant en ENE
        pass

    def student_BIO(self):
        # Logique pour créer un étudiant en BIO
        pass

    def student_INF(self):
        # Logique pour créer un étudiant en INF
        pass

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
