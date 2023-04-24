class Animal:
    def __init__(self):
        self.age = 0
        self.nom = ""

    def vieillir(self):
        self.age += 1

# Instancier un objet Animal
mon_animal = Animal()

# Afficher l'âge initial de l'animal
print("Age initial de l'animal : ", mon_animal.age)

# Faire vieillir l'animal et afficher son âge
mon_animal.vieillir()
print("Age de l'animal après avoir vieilli : ", mon_animal.age)


