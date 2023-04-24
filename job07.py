class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

    def get_titre(self):
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_nb_pages(self):
        return self._nb_pages

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0 and isinstance(nb_pages, int):
            self._nb_pages = nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

    def afficher_livre(self):
        print(f"Titre : {self._titre}")
        print(f"Auteur : {self._auteur}")
        print(f"Nombre de pages : {self._nb_pages}")
