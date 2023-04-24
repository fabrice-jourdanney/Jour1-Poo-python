class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(resultat)
op = Operation(4, 6)
op.addition()  # affiche 10 dans la console
