class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = False
        self.reservoir = 50

    # Mutateurs et accesseurs pour chaque attribut
    def set_marque(self, marque):
        self.marque = marque

    def get_marque(self):
        return self.marque

    def set_modele(self, modele):
        self.modele = modele

    def get_modele(self):
        return self.modele

    def set_annee(self, annee):
        self.annee = annee

    def get_annee(self):
        return self.annee

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def get_kilometrage(self):
        return self.kilometrage

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def get_en_marche(self):
        return self.en_marche

    # Méthodes pour démarrer et arrêter la voiture
    def demarrer(self):
        if self.verifier_plein():
            self.en_marche = True
        else:
            print("Le réservoir est presque vide. Impossible de démarrer.")

    def arreter(self):
        self.en_marche = False

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        if self.reservoir > 5:
            return True
        else:
            return False
voiture1 = Voiture("Renault", "Clio", 2018, 30000)

# Affichage des attributs initiaux de la voiture
print("Marque :", voiture1.get_marque())
print("Modèle :", voiture1.get_modele())
print("Année :", voiture1.get_annee())
print("Kilométrage :", voiture1.get_kilometrage())
print("En marche :", voiture1.get_en_marche())

# Démarrage de la voiture
voiture1.demarrer()
print("En marche :", voiture1.get_en_marche())

# Arrêt de la voiture
voiture1.arreter()
print("En marche :", voiture1.get_en_marche())

# Modification du niveau du réservoir
voiture1.reservoir = 4
voiture1.demarrer()
