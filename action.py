import random

# --- Classe Arme ---
class Arme:
    def __init__(self, nom, degats, type_degats):
        self.nom = nom
        self.degats = degats
        self.type_degats = type_degats

    def lancer_degats(self):
        return random.randint(1, self.degats)

# --- Fonction attaque ---
def attaque(lanceur, cible):
    print(f"{lanceur.nom} attaque {cible.nom}")
    jet = random.randint(1,20)
    print("Jet d'attaque :", jet)

    if jet == 20:
        print("Réussite critique !")
        degats = lanceur.degats() * 2
    elif jet == 1:
        print("Échec critique !")
        degats = lanceur.degats()
        lanceur.pv -= degats
        print(lanceur.nom, "se blesse lui-même")
        return
    elif jet >= cible.defense:
        print("L'attaque touche")
        degats = lanceur.degats()
    else:
        print("L'attaque échoue")
        return

    if hasattr(cible, "resistances") and lanceur.arme.type_degats in getattr(cible, "resistances", []):
        print("Résistance ! dégâts divisés par 2")
        degats = degats // 2

    cible.pv -= degats
    print(cible.nom, "perd", degats, "PV et a maintenant", cible.pv, "PV")

# --- Classes Creature, Hero, Monstre ---
class Creature:
    def __init__(self, nom, pv, defense):
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.initiative = 0

    def est_vivant(self):
        return self.pv > 0

class Hero(Creature):
    def __init__(self, nom, pv, defense, arme):
        super().__init__(nom, pv, defense)
        self.arme = arme

    def degats(self):
        return self.arme.lancer_degats()

class Monstre(Creature):
    def __init__(self, nom, pv, defense, type_degats, resistances=[]):
        super().__init__(nom, pv, defense)
        self.type_degats = type_degats
        self.resistances = resistances

    def degats(self):
        return random.randint(1, 8)  # exemple 1d8 pour monstre
