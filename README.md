# Projet-POOB1 — Système de combat RPG

## Description

Application Python en ligne de commande permettant à un Maître du Jeu de gérer des combats de type Donjons et Dragons. Le MJ sélectionne les héros et les monstres, et le programme gère automatiquement tous les jets de dés, l'ordre de jeu et les résultats des actions.

## Prérequis

- Python 3.x installé sur votre machine
- Aucune bibliothèque externe nécessaire


## Comment jouer

1. Le programme demande combien de héros vont combattre
2. Pour chaque héros, on choisit un personnage dans la liste puis une arme
3. Le programme demande combien de monstres vont combattre
4. Pour chaque monstre, on choisit un monstre dans la liste
5. L'initiative est lancée automatiquement pour déterminer l'ordre de jeu
6. Le combat se déroule tour par tour jusqu'à la victoire ou la défaite

## Actions disponibles en combat

- **Attaque** — Lance 1d20, si le résultat dépasse la défense de la cible l'attaque touche et inflige des dégâts
- **Soin** — Soigne un allié de 2d8 points de vie sans jet de dé
- **Buff** — Augmente la défense d'un allié de +3 points
- **Debuff** — Réduit la défense d'un ennemi de -3 points

## Règles spéciales

- **Réussite critique** — Si le jet d'attaque donne 20, les dégâts sont doublés
- **Échec critique** — Si le jet d'attaque donne 1, la créature se blesse elle-même
- **Résistances** — Certains monstres résistent à certains types de dégâts, les dégâts sont alors divisés par 2

## Fonctionnalités supplémentaires

### Système de météo

Au début de chaque combat une météo est choisie aléatoirement parmi 4 possibilités. La météo influence les dégâts de certains types d'attaques pendant toute la durée du combat.

- **Soleil** — booste les attaques de Feu de +2 et pénalise les attaques de Glace de -2
- **Pluie** — pénalise les attaques de Feu de -2 et booste les attaques Perçantes de +1
- **Orage** — booste les attaques Magiques de +2 et pénalise les attaques de Feu de -1
- **Neige** — booste les attaques Tranchantes de +1 et pénalise les attaques de Feu de -3

Par exemple si la météo est Neige et qu'un héros attaque avec une épée (dégâts Tranchants), il fera +1 dégât supplémentaire. Si un dragon attaque avec du Feu, il fera -3 dégâts à cause de la neige qui éteint ses flammes.

La météo s'applique automatiquement à chaque attaque et un message informe le MJ si les dégâts ont été modifiés.

### Système de pièges

Au début de chaque round, le programme lance secrètement un dé à 6 faces. Si le résultat est 6, un piège se déclenche automatiquement sur une créature choisie au hasard parmi tous les combattants encore en vie.

Le piège inflige 1d6 dégâts à la créature touchée, que ce soit un héros ou un monstre. Cela ajoute un élément de surprise et d'imprévu au combat car personne n'est à l'abri, ni les héros ni les monstres.

La probabilité qu'un piège se déclenche est de 1 chance sur 6 à chaque round.

## Structure du projet

- `classe_creature.py` — Classes Creature, Hero, Monstre et les catalogues
- `arme.py` — Classes Arme et Action, fonction lancer_des et catalogue des armes
- `fonctionnalites.py` — Système de météo et système de pièges
- `interface.py` — Interface utilisateur et boucle de combat principale
- `main.py` — Code complet pour faire marcher tout le jeu

