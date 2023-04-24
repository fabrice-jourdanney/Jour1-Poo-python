class Student:
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print("Le nombre de crédits doit être supérieur à zéro.")
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien."
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Identifiant: {self.__id}")
        print(f"Niveau: {self.__level}")
        print(f"Crédits: {self.__credits}")


# Instanciation de l'objet John Doe avec l'identifiant 145
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à John Doe
john_doe.add_credits(30)
john_doe.add_credits(40)
john_doe.add_credits(20)

# Affichage des informations de John Doe
john_doe.studentInfo()

