import random
from classes_creatures import Creature, Hero, Monstre, CATALOGUE_HEROS, CATALOGUE_MONSTRES
from classes_arme_action import lancer_des, Arme, Action, CATALOGUE_ARMES
from fonctionnalites import choisir_meteo, appliquer_meteo, declencher_piege

print("Bienvenue dans le système de combat RPG")


def saisir_entier(message, min_val, max_val):
    while True:
        try:
            valeur = int(input(message))
            if valeur >= min_val and valeur <= max_val:
                return valeur
            else:
                print("Entrez un nombre entre", min_val, "et", max_val)
        except ValueError:
            print("Entrez un nombre valide.")


nb_heros = saisir_entier(
    "Combien de héros vont combattre ? ", 1, len(CATALOGUE_HEROS))

heros = []

for i in range(nb_heros):
    print("\nHéros", i + 1)

    for j, hero in enumerate(CATALOGUE_HEROS, 1):
        print(j, "-", hero["nom"], "-", hero["description"],
              "- PV:", hero["pv"], "- Défense:", hero["defense"])

    choix = saisir_entier("Choisissez un héros : ", 1, len(CATALOGUE_HEROS))
    hero_choisi = CATALOGUE_HEROS[choix - 1]

    for j, arme in enumerate(CATALOGUE_ARMES, 1):
        print(j, "-", arme.nom, "-", arme.nb_des,
              "d", arme.faces, "-", arme.type_degats)

    choix_arme = saisir_entier(
        "Choisissez une arme : ", 1, len(CATALOGUE_ARMES))
    arme_choisie = CATALOGUE_ARMES[choix_arme - 1]

    hero = Hero(hero_choisi["nom"], hero_choisi["description"],
                hero_choisi["pv"], hero_choisi["defense"], arme_choisie)
    heros.append(hero)

nb_monstres = saisir_entier(
    "Combien de monstres vont combattre ? ", 1, len(CATALOGUE_MONSTRES))

monstres = []

for i in range(nb_monstres):
    print("\nMonstre", i + 1)

    for j, monstre in enumerate(CATALOGUE_MONSTRES, 1):
        print(j, "-", monstre.nom, "-", monstre.description,
              "- PV:", monstre.pv, "- Défense:", monstre.defense)

    choix = saisir_entier("Choisissez un monstre : ",
                          1, len(CATALOGUE_MONSTRES))
    monstre_choisi = CATALOGUE_MONSTRES[choix - 1]
    monstres.append(monstre_choisi)

print("\n--- INITIATIVE ---")

for hero in heros:
    hero.initiative = lancer_des(1, 20)
    print(hero.nom, ":", hero.initiative)

for monstre in monstres:
    monstre.initiative = lancer_des(1, 20)
    print(monstre.nom, ":", monstre.initiative)

toutes_creatures = heros + monstres

for i in range(len(toutes_creatures) - 1):
    for j in range(i + 1, len(toutes_creatures)):
        if toutes_creatures[j].initiative > toutes_creatures[i].initiative:
            temp = toutes_creatures[i]
            toutes_creatures[i] = toutes_creatures[j]
            toutes_creatures[j] = temp
print("\n--- ORDRE DE JEU ---")
for creature in toutes_creatures:
    print(creature.nom, ":", creature.initiative)

meteo = choisir_meteo()

print("\n--- COMBAT ---")

combat_en_cours = True

while combat_en_cours:
    print("\n--- Nouveau round ---")
    declencher_piege(toutes_creatures)

    for creature in toutes_creatures:
        if creature.est_vivant():
            print("\nC'est au tour de", creature.nom)
            print("1 - Attaque")
            print("2 - Soin")
            print("3 - Buff (augmente la défense d'un allié de +3)")
            print("4 - Debuff (réduit la défense d'un ennemi de -3)")
            choix_action = saisir_entier("Choisissez une action : ", 1, 4)

            if choix_action == 1:
                print("\nChoisissez une cible :")
                if creature in heros:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]
                else:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]

                jet = lancer_des(1, 20)
                print(creature.nom, "lance 1d20 :", jet)

                if creature in heros:
                    degats_normaux = creature.arme.lancer_degats()
                else:
                    degats_normaux = lancer_des(
                        creature.nb_des, creature.faces)

                degats_normaux = appliquer_meteo(
                    degats_normaux, creature.type_degats, meteo)

                if jet == 1:
                    creature.pv = creature.pv - degats_normaux
                    print("Echec critique !", creature.nom, "se blesse pour",
                          degats_normaux, "dégâts. PV restants :", creature.pv)

                elif jet == 20:
                    degats = degats_normaux * 2
                    if creature.type_degats in cible.resistances:
                        degats = degats // 2
                        print("Résistance !", cible.nom,
                              "résiste et ne subit que", degats, "dégâts.")
                    cible.pv = cible.pv - degats
                    print("Réussite critique !", cible.nom, "subit",
                          degats, "dégâts. PV restants :", cible.pv)

                elif jet > cible.defense:
                    if creature.type_degats in cible.resistances:
                        degats_normaux = degats_normaux // 2
                        print("Résistance !", cible.nom,
                              "résiste et ne subit que", degats_normaux, "dégâts.")
                    cible.pv = cible.pv - degats_normaux
                    print("Touché !", cible.nom, "subit", degats_normaux,
                          "dégâts. PV restants :", cible.pv)

                else:
                    print("Raté ! Le jet", jet, "est inférieur à la défense de",
                          cible.nom, "(", cible.defense, ")")

            elif choix_action == 2:
                print("\nChoisissez une cible à soigner :")
                if creature in heros:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]
                else:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- PV:", c.pv)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]

                soin = lancer_des(2, 8)
                cible.pv = cible.pv + soin
                print(creature.nom, "soigne", cible.nom, "de",
                      soin, "PV. PV restants :", cible.pv)

            elif choix_action == 3:
                print("\nChoisissez un allié à booster :")
                if creature in heros:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]
                else:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]

                cible.defense = cible.defense + 3
                print(creature.nom, "booste la défense de", cible.nom,
                      "de +3. Défense maintenant :", cible.defense)

            elif choix_action == 4:
                print("\nChoisissez un ennemi à affaiblir :")
                if creature in heros:
                    monstres_vivants_liste = []
                    for m in monstres:
                        if m.est_vivant():
                            monstres_vivants_liste.append(m)
                    for j, c in enumerate(monstres_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(monstres_vivants_liste))
                    cible = monstres_vivants_liste[choix_cible - 1]
                else:
                    heros_vivants_liste = []
                    for h in heros:
                        if h.est_vivant():
                            heros_vivants_liste.append(h)
                    for j, c in enumerate(heros_vivants_liste, 1):
                        print(j, "-", c.nom, "- Défense:", c.defense)
                    choix_cible = saisir_entier(
                        "Votre choix : ", 1, len(heros_vivants_liste))
                    cible = heros_vivants_liste[choix_cible - 1]

                cible.defense = cible.defense - 3
                print(creature.nom, "affaiblit la défense de", cible.nom,
                      "de -3. Défense maintenant :", cible.defense)

    heros_vivants = 0
    for hero in heros:
        if hero.est_vivant():
            heros_vivants += 1

    monstres_vivants = 0
    for monstre in monstres:
        if monstre.est_vivant():
            monstres_vivants += 1

    if heros_vivants == 0:
        print("\nDéfaite ! Tous les héros sont morts.")
        combat_en_cours = False

    elif monstres_vivants == 0:
        print("\nVictoire ! Tous les monstres sont vaincus !")
        combat_en_cours = False

