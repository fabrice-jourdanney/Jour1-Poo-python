class Rectangle:
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
# Création d'un rectangle avec longueur 10 et largeur 5
mon_rectangle = Rectangle(10, 5)

# Affichage des valeurs initiales
print("Longueur du rectangle :", mon_rectangle.get_longueur())
print("Largeur du rectangle :", mon_rectangle.get_largeur())

# Modification des valeurs
mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(7)

# Affichage des nouvelles valeurs
print("Longueur du rectangle après modification :", mon_rectangle.get_longueur())
print("Largeur du rectangle après modification :", mon_rectangle.get_largeur())

