import random


METEOS = {
    "Soleil":  {"Feu": 2, "Glace": -2},
    "Pluie":   {"Feu": -2, "Perçant": 1},
    "Orage":   {"Magique": 2, "Feu": -1},
    "Neige":   {"Tranchant": 1, "Feu": -3},
}
import random


METEOS = {
    "Soleil":  {"Feu": 2, "Glace": -2},
    "Pluie":   {"Feu": -2, "Perçant": 1},
    "Orage":   {"Magique": 2, "Feu": -1},
    "Neige":   {"Tranchant": 1, "Feu": -3},
}


def choisir_meteo():
    meteo = random.choice(list(METEOS.keys()))
    print("\nMétéo du combat :", meteo)
    effets = METEOS[meteo]
    for type_degats, bonus in effets.items():
        if bonus > 0:
            print(" +", bonus, "dégâts pour les attaques de type", type_degats)
        else:
            print(" ", bonus, "dégâts pour les attaques de type", type_degats)
    return meteo


def appliquer_meteo(degats, type_degats, meteo):
    effets = METEOS[meteo]
    if type_degats in effets:
        bonus = effets[type_degats]
        degats = degats + bonus
        if bonus > 0:
            print("La météo booste les dégâts de", bonus, "!")
        else:
            print("La météo réduit les dégâts de", abs(bonus), ".")
    if degats < 1:
        degats = 1
    return degats


def declencher_piege(toutes_creatures):
    jet = random.randint(1, 6)
    if jet == 6:
        creatures_vivantes = []
        for c in toutes_creatures:
            if c.est_vivant():
                creatures_vivantes.append(c)
        cible = random.choice(creatures_vivantes)
        degats = random.randint(1, 6)
        cible.pv = cible.pv - degats
        print("\nPiège !", cible.nom, "tombe dans un piège et subit",
              degats, "dégâts. PV restants :", cible.pv)