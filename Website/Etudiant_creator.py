import random
import csv

class Etudiant:
    def __init__(self,filiere):
        # self.nom                 = nom
        # self.prenom              = prenom
        self.filiere             = filiere
        self.domaine_interets    = {"Automotive": 0,"Environment": 0,"Construction": 0,"Tourism": 0,"Communication":0,"Finance":0,"Education":0,"Energy":0,"Farming":0,"Telecom":0,"Pharmaceutical":0,"Media":0,"Logistics":0,"Aerospace":0}
        self.niveau_outils       = {"Matlab" : 0,"Python": 0,"C": 0,"Microcontrolleur": 0,"VHDL": 0,"Microprocesseur": 0,"Electronique": 0,"Probabilite": 0,"Reseau": 0,"IA": 0}
        self.interet_entreprises = entreprises = {
            "Thales": 0,
            "Orange": 0,
            "Siemens": 0,
            "Engie": 0,
            "Safran": 0,
            "Renault": 0,
            "Dassault systeme": 0,
            "BNP Paribas": 0,
            "Loreal": 0,
            "EQUANS": 0
        }

        self.niveau_matiere = {
            'Information_Analogique': 0,
            'Programmation_Python': 0,
            'Programmation_Java': 0,
            'Programmation_C': 0,
            'Traitement_du_signal': 0,
            'Microprocesseurs': 0,
            'Electronique_Numerique': 0,
            'Electronique_Analogique': 0,
            'Probabilite': 0,
            'Algortihmique': 0,
            'Reseaux': 0,
            'Optimisation_et_IA': 0,
            'Base_de_donnees': 0,
            'Systeme_Dynamique': 0,
            'Microcontroleurs': 0
        }

        self.choix_ouap_E = {
            'EL-3012': 0,
            'EL-3013': 0,
            'EL-3019': 0,
            'EL-3020': 0,
            'EL-3025': 0,
            'EL-3031': 0,
            'EL-3035': 0,
        }

        self.choix_ouap_F = {
            'EL-3017': 0,
            'EL-3034':0,
            'EL-3003':0,
            'EL-3005':0,
            'EL-3007':0,
            'EL-3023':0,
            'EL-3027':0
        }

    def create_student(self):
        method_name = f"student_{self.filiere}"
        if hasattr(self, method_name):
            return getattr(self, method_name)()
        else:
            return self.student_default()


    def student_DSI(self):

        self.interet_entreprises["Thales"] = random.choices([1, 0], weights=[0.345, 0.655])[0]
        self.interet_entreprises["Orange"] = random.choices([1, 0], weights=[0.691, 0.309])[0]
        self.interet_entreprises["Siemens"] = random.choices([1, 0], weights=[0.945, 0.055])[0]
        self.interet_entreprises["Engie"] = random.choices([1, 0], weights=[0.927, 0.073])[0]
        self.interet_entreprises["Safran"] = random.choices([1, 0], weights=[0.564, 0.436])[0]
        self.interet_entreprises["Renault"] = random.choices([1, 0], weights=[0.818, 0.182])[0]
        self.interet_entreprises["Dassault systeme"] = random.choices([1, 0], weights=[0.527, 0.473])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([1, 0], weights=[0.436, 0.564])[0]
        self.interet_entreprises["Loreal"] = random.choices([1, 0], weights=[0.673, 0.327])[0]
        self.interet_entreprises["EQUANS"] = random.choices([1, 0], weights=[0.964, 0.036])[0]
        
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

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0.1,0.047619048,0.527272727,0,	0.2,0.117647059,0.058823529])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.5625,	0.083333333,0.115384615,0.086956522,0.090909091,0.058823529,0.181818182])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0

    def student_AIC(self):
        self.domaine_interets["Automotive"] = random.choices([1, 2, 3, 4, 5], weights=[0.211, 0.211, 0.211, 0.263, 0.105])[0]
        self.domaine_interets["Environment"] = random.choices([1, 2, 3, 4, 5], weights=[0.211, 0.158, 0.316, 0.263, 0.053])[0]
        self.domaine_interets["Construction"] = random.choices([1, 2, 3, 4, 5], weights=[0.579, 0.105, 0.263, 0.053, 0.0])[0]
        self.domaine_interets["Tourism"] = random.choices([1, 2, 3, 4, 5], weights=[0.421, 0.105, 0.158, 0.263, 0.053])[0]
        self.domaine_interets["Communication"] = random.choices([1, 2, 3, 4, 5], weights=[0.0, 0.053, 0.158, 0.421, 0.368])[0]
        self.domaine_interets["Finance"] = random.choices([1, 2, 3, 4, 5], weights=[0.211, 0.105, 0.211, 0.263, 0.211])[0]
        self.domaine_interets["Education"] = random.choices([1, 2, 3, 4, 5], weights=[0.158, 0.263, 0.263, 0.158, 0.158])[0]
        self.domaine_interets["Energy"] = random.choices([1, 2, 3, 4, 5], weights=[0.368, 0.211, 0.211, 0.105, 0.105])[0]
        self.domaine_interets["Farming"] = random.choices([1, 2, 3, 4, 5], weights=[0.526, 0.263, 0.211, 0.0, 0.0])[0]
        self.domaine_interets["Telecom"] = random.choices([1, 2, 3, 4, 5], weights=[0.105, 0.211, 0.526, 0.158, 0.0])[0]
        self.domaine_interets["Pharmaceutical"] = random.choices([1, 2, 3, 4, 5], weights=[0.421, 0.263, 0.105, 0.158, 0.053])[0]
        self.domaine_interets["Media"] = random.choices([1, 2, 3, 4, 5], weights=[0.053, 0.105, 0.316, 0.526, 0.0])[0]
        self.domaine_interets["Logistics"] = random.choices([1, 2, 3, 4, 5], weights=[0.158, 0.368, 0.316, 0.158, 0.0])[0]
        self.domaine_interets["Aerospace"] = random.choices([1, 2, 3, 4, 5], weights=[0.105, 0.053, 0.211, 0.316, 0.316])[0]

        
        self.interet_entreprises = {
            "Thales": random.choices([1, 0], weights=[0.895, 0.105])[0],
            "Orange": random.choices([1, 0], weights=[0.368, 0.632])[0],
            "Siemens": random.choices([1, 0], weights=[0.053, 0.947])[0],
            "Engie": random.choices([1, 0], weights=[0.053, 0.947])[0],
            "Safran": random.choices([1, 0], weights=[0.526, 0.474])[0],
            "Renault": random.choices([1, 0], weights=[0.263, 0.737])[0],
            "Dassault systeme": random.choices([1, 0], weights=[0.579, 0.421])[0],
            "BNP Paribas": random.choices([1, 0], weights=[0.421, 0.579])[0],
            "Loreal": random.choices([1, 0], weights=[0.105, 0.895])[0],
            "EQUANS": random.choices([1, 0], weights=[0, 0.1])[0]
        }
        
        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0.15,0.095238095,0.127272727,0.111111111,0.3,0,0])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.145833333,0,	0.076923077,0.260869565,0.090909091,0,0.136363636])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0



    def student_CYB(self):
        self.domaine_interets["Automotive"]   = random.choices([1,2,3,4,5], weights=[0.217 ,0.239,0.239 ,0.217,0.087])[0]
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
            "Loreal": random.choices([1, 0], weights=[0.13, 0.87])[0],
            "EQUANS": random.choices([1, 0], weights=[0.109, 0.891])[0]
        }
        
        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0.45,0.047619048,0.072727273,0,0.25,0,0.058823529])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.104166667,0.083333333,0.038461538,0.304347826,0.181818182,0,0.181818182])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0

    def student_GI_(self):
        self.domaine_interets["Automotive"]      = random.choices([1,2,3,4,5], weights=[0.114 ,0.114,0.171 ,0.343,0.257])[0]
        self.domaine_interets["Environment"]    = random.choices([1,2,3,4,5], weights=[0.057 ,0.200,0.286,0.343,0.114])[0]
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
        self.interet_entreprises["Dassault systeme"] = random.choices([0,1], weights=[0.429, 0.571])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0,1], weights=[1, 0])[0]
        self.interet_entreprises["Loreal"] = random.choices([0,1], weights=[0.543, 0.457])[0]
        self.interet_entreprises["EQUANS"] = random.choices([0,1], weights=[0.914, 0.086])[0]

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0,0.095238095,0.145454545,0,0.05,0.117647059,0.058823529])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.020833333,0.083333333,0.038461538,0.130434783,0.454545455,0.176470588,0])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0

    def student_SE_(self):
        # Logique pour créer un étudiant en SE
        self.domaine_interets["Automotive"]      = random.choices([1,2,3,4,5], weights=[0.071, 0.107, 0.286, 0.250, 0.286])[0]
        self.domaine_interets["Environment"]    = random.choices([1,2,3,4,5], weights=[0.089, 0.286, 0.357, 0.179, 0.089])[0]
        self.domaine_interets["Construction"]     = random.choices([1,2,3,4,5], weights=[0.357, 0.357, 0.196, 0.071, 0.018])[0]
        self.domaine_interets["Tourism"]          = random.choices([1,2,3,4,5], weights=[0.518, 0.232, 0.143, 0.071, 0.036])[0]
        self.domaine_interets["Communication"]    = random.choices([1,2,3,4,5], weights=[0.054, 0.250, 0.375, 0.071, 0.250])[0]
        self.domaine_interets["Finance"]          = random.choices([1,2,3,4,5], weights=[0.339, 0.250, 0.268, 0.071, 0.071])[0]
        self.domaine_interets["Education"]        = random.choices([1,2,3,4,5], weights=[0.268, 0.304, 0.232, 0.161, 0.036])[0]
        self.domaine_interets["Energy"]           = random.choices([1,2,3,4,5], weights=[0.143, 0.375, 0.214, 0.232, 0.036])[0]
        self.domaine_interets["Farming"]          = random.choices([1,2,3,4,5], weights=[0.482, 0.232, 0.196, 0.054, 0.036])[0]
        self.domaine_interets["Telecom"]          = random.choices([1,2,3,4,5], weights=[0.179, 0.393, 0.250, 0.125, 0.054])[0]
        self.domaine_interets["Pharmaceutical"]   = random.choices([1,2,3,4,5], weights=[0.518, 0.250, 0.125, 0.089, 0.018])[0]
        self.domaine_interets["Media"]            = random.choices([1,2,3,4,5], weights=[0.179, 0.161, 0.339, 0.161, 0.161])[0]
        self.domaine_interets["Logistics"]        = random.choices([1,2,3,4,5], weights=[0.179, 0.143, 0.214, 0.268, 0.196])[0]
        self.domaine_interets["Aerospace"]        = random.choices([1,2,3,4,5], weights=[0.054, 0.054, 0.107, 0.125, 0.661])[0]

        self.interet_entreprises["Thales"] = random.choices([0,1], weights=[0.286, 0.714])[0]
        self.interet_entreprises["Orange"] = random.choices([0,1], weights=[0.929, 0.071])[0]
        self.interet_entreprises["Siemens"] = random.choices([0,1], weights=[0.661, 0.339])[0]
        self.interet_entreprises["Engie"] = random.choices([0,1], weights=[0.964, 0.036])[0]
        self.interet_entreprises["Safran"] = random.choices([0,1], weights=[0.232, 0.768])[0]
        self.interet_entreprises["Renault"] = random.choices([0,1], weights=[0.643, 0.357])[0]
        self.interet_entreprises["Dassault systeme"] = random.choices([0,1], weights=[0.357, 0.643])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0,1], weights=[0.946, 0.054])[0]
        self.interet_entreprises["Loreal"] = random.choices([0,1], weights=[0.929, 0.071])[0]
        self.interet_entreprises["EQUANS"] = random.choices([0,1], weights=[1, 0])[0]

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0,0.19047619,0.018181818,0.555555556,0.05,0,0.117647059])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.041666667,0.083333333,0.307692308,0,0,0.058823529,0.045454545])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0

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
        self.interet_entreprises["Loreal"] = random.choices([1, 0], weights=[0.8, 0.2])[0]
        self.interet_entreprises["EQUANS"] = random.choices([1, 0], weights=[1.0, 0.0])[0]

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0.05,0.523809524,0.036363636,0.111111111,0,0,0])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.0625,0,0.269230769,0.130434783,0.090909091,0,0.045454545])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0


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
        self.interet_entreprises["Dassault systeme"] = random.choices([0, 1], weights=[0.710, 0.290])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0, 1], weights=[0.839, 0.161])[0]
        self.interet_entreprises["Loreal"] = random.choices([0, 1], weights=[0.935, 0.065])[0]
        self.interet_entreprises["EQUANS"] = random.choices([0, 1], weights=[0.613, 0.387])[0]

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0,0,0,0,0.05,0.058823529,0.6470588240])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0,0.666666667,0.038461538,0,0,0.117647059,0.090909091])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0

    
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
        self.interet_entreprises["Loreal"] = random.choices([1, 0], weights=[0.292, 0.708])[0]
        self.interet_entreprises["EQUANS"] = random.choices([1, 0], weights=[1.0, 0.0])[0]

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0,0,0.018181818,0.111111111,0.05,0.647058824,0.058823529])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.041666667,0,0.076923077,0,0.090909091,0.588235294,0])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0

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
        self.interet_entreprises["Dassault systeme"] = random.choices([0, 1], weights=[0.514, 0.486])[0]
        self.interet_entreprises["BNP Paribas"] = random.choices([0, 1], weights=[0.622, 0.378])[0]
        self.interet_entreprises["Loreal"] = random.choices([0, 1], weights=[0.919, 0.081])[0]
        self.interet_entreprises["EQUANS"] = random.choices([0, 1], weights=[1.000, 0.000])[0]

        Choix_E = random.choices([ 'EL-3012','EL-3013','EL-3019','EL-3020','EL-3025','EL-3031','EL-3035'], weights=[0.25,0,0.054545455,0.111111111,0.05,0.058823529,0])[0]
        
        for ouap in self.choix_ouap_E:
            if ouap == Choix_E:
                self.choix_ouap_E[ouap] = 1
            else:
                self.choix_ouap_E[ouap] = 0

        Choix_F = random.choices(['EL-3003','EL-3005','EL-3007','EL-3017','EL-3023','EL-3027','EL-3034'], weights=[0.020833333,0,0.038461538,0.086956522,0,0,0.318181818])[0]

        for ouapF in self.choix_ouap_F:
            if ouapF == Choix_F:
                self.choix_ouap_F[ouapF] = 1
            else:
                self.choix_ouap_F[ouapF] = 0



    def student_default(self):
        # Logique pour créer un étudiant par défaut
        pass


# # Exemple d'utilisation :
# etudiant1 = Etudiant("nom","prenom", "DSIA")
# etudiant1.create_student()
# print("Nom:", etudiant1.nom)
# print("Prénom:", etudiant1.prenom)
# print("Filière:", etudiant1.filiere)
# print("Domaines d'intérêt:", etudiant1.domaine_interets)
# print("Niveau d'outils:", etudiant1.niveau_outils)
# print("Intérêt pour les entreprises:", etudiant1.interet_entreprises)

def save_students_to_csv(filename, students):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # En-tête du CSV avec les noms des entreprises et des domaines
        header = ['Filiere'] + list(students[0].interet_entreprises.keys()) + list(students[0].domaine_interets.keys())+ list(students[0].choix_ouap_E.keys())+ list(students[0].choix_ouap_F.keys())
        writer.writerow(header)
        
        for student in students:
            row = [student.filiere] + list(student.interet_entreprises.values()) + list(student.domaine_interets.values()) + list(student.choix_ouap_E.values())+ list(student.choix_ouap_F.values())
            writer.writerow(row)

def generator_student():
    effectif = 500
    # Générer 100 étudiants de la filière DSIA
    students_bio = [Etudiant("BIO") for _ in range(effectif)]
    for student in students_bio:
        student.create_student()

    students_cyb = [Etudiant("CYB") for _ in range(effectif)]
    for student in students_cyb:
        student.create_student()

    students_aic = [Etudiant("AIC") for _ in range(effectif)]
    for student in students_aic :
        student.create_student()

    students_inf = [Etudiant("INF") for _ in range(effectif)]
    for student in students_inf:
        student.create_student()

    students_gi = [Etudiant("GI_") for _ in range(effectif)]
    for student in students_gi :
        student.create_student()


    students_dsi = [Etudiant("DSI") for _ in range(effectif)]
    for student in students_dsi :
        student.create_student()



    students_sei = [Etudiant("SEI") for _ in range(effectif)]
    for student in students_sei :
        student.create_student()


    students_se = [Etudiant("SE_") for _ in range(effectif)]
    for student in students_se :
        student.create_student()


    students_ene = [Etudiant("ENE") for _ in range(effectif)]
    for student in students_ene :
        student.create_student()

    all_students = students_dsi + students_sei + students_se + students_cyb + students_aic + students_inf + students_bio + students_ene + students_gi
    # Enregistrer les étudiants dans un fichier CSV
    save_students_to_csv('etudiants.csv', all_students)
