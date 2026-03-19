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


CATALOGUE_HEROS = [
    {"nom": "Guerrier", "description": "Brave combattant proche du corps à corps",
        "pv": 35, "defense": 12},
    {"nom": "Magicien", "description": "Maître de la magie offensive",
        "pv": 25, "defense": 10},
    {"nom": "Archer", "description": "Expert du combat à distance",
        "pv": 28, "defense": 11},
    {"nom": "Paladin", "description": "Guerrier sacré protecteur",
        "pv": 40, "defense": 14},
    {"nom": "Assassin", "description": "Combattant furtif et rapide",
        "pv": 26, "defense": 13},
]

CATALOGUE_MONSTRES = [
    Monstre("Gobelin", "Petite créature rusée", 18, 9, "Perçant", 1, 4),
    Monstre("Squelette", "Guerrier mort-vivant", 25, 10, "Tranchant", 1, 6),
    Monstre("Dragon", "Seigneur des flammes", 60, 16, "Feu", 3, 8, ["Feu"]),
    Monstre("Loup", "Bête sauvage agile", 22, 10, "Tranchant", 1, 6),
]
