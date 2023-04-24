# Définir la classe "Operation"
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Créer une instance de la classe "Operation"
op = Operation(10, 5)

# Imprimer les valeurs des attributs "nombre1" et "nombre2"
print("Nombre 1 :", op.nombre1)
print("Nombre 2 :", op.nombre2)
