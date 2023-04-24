class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je m'appelle {self.prenom} {self.nom}"
personne1 = Personne("Voyage", "Fabrice")
print(personne1.SePresenter())  # affiche "Je m'appelle Fabrice Voyage"

personne2 = Personne("Narisara", "Rung")
print(personne2.SePresenter())  # affiche "Je m'appelle Rung Narisara"
