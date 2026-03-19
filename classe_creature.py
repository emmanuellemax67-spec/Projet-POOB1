class Creature:

    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.actions = []
        self.initiative = 0
        self.resistances = []


class Hero(Creature):

    def __init__(self, nom, description, pv, defense, arme):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = arme.type_degats
        self.actions = []
        self.initiative = 0
        self.resistances = []
        self.arme = arme

    def afficher_caracteristiques(self):
        print("\n--- HÉROS ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.type_degats)
        print("Arme :", self.arme.nom)


class Monstre(Creature):

    def __init__(self, nom, description, pv, defense, type_degats, nb_des, faces, resistances=None):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.actions = []
        self.initiative = 0
        self.nb_des = nb_des
        self.faces = faces
        if resistances is None:
            resistances = []
        self.resistances = resistances

    def afficher_caracteristiques(self):
        print("\n--- MONSTRE ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.type_degats)
        print("Résistances :", self.resistances)
