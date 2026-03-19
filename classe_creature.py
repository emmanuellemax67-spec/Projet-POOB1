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
