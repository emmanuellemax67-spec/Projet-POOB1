import random


def lancer_des(nb_des, faces):
    total = 0
    for i in range(nb_des):
        total += random.randint(1, faces)
    return total


class Arme:

    def __init__(self, nom, nb_des, faces, type_degats):
        self.nom = nom
        self.nb_des = nb_des
        self.faces = faces
        self.type_degats = type_degats

    def lancer_degats(self):
        return lancer_des(self.nb_des, self.faces)


class Action:

    def __init__(self, nom):
        self.nom = nom


CATALOGUE_ARMES = [
    Arme("Epée", 1, 8, "Tranchant"),
    Arme("Dague", 1, 4, "Perçant"),
    Arme("Hache", 2, 6, "Tranchant"),
    Arme("Arc", 1, 8, "Perçant"),
    Arme("Marteau", 2, 6, "Contondant"),
    Arme("Bâton", 1, 6, "Magique"),
]