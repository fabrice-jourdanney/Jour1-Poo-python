class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.__disponible = disponible

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.vérification():
            self.__disponible = False
            print("Le livre", self.titre, "a été emprunté.")
        else:
            print("Le livre", self.titre, "n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.vérification():
            self.__disponible = True
            print("Le livre", self.titre, "a été rendu.")
        else:
            print("Le livre", self.titre, "n'a pas été emprunté.")
