Dania Ait Mammar 
INTRODUCTION: 
Voici mon deuxième projet de INF1007. Voici les instructions pour la conception d'un pacman.

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/w0u_3EH_)
# Projet 2 - Programmation orientée objet avec un jeu Pacman 🟡

## Directives

## Introduction
Pacman, jeu d'arcade emblématique et intemporel, constitue un excellent moyen d'explorer les concepts de programmation orientée objet. Dans ce projet, vous découvrirez une implémentation complète du jeu utilisant les principes de programmation orientée objet avec Python et la bibliothèque Pygame.

## Installations requises
Ce projet nécessite l'utilisation de la bibliothèque [`pygame`](https://www.pygame.org/wiki/about), qui permet de créer facilement des interfaces de jeu en Python. Vous pouvez installer pygame avec la commande suivante dans votre terminal :

```bash
python3 -m pip install -U pygame==2.6.0
```

## Détails sur le jeu

Cette implémentation complète de Pacman inclut :
- **Contrôle du joueur** : Pacman peut être déplacé avec les touches fléchées
- **Comportement automatique des fantômes** : Quatre fantômes avec des comportements uniques
- **Système de score** : Points pour les dots, power pellets et fantômes
- **États de jeu** : Menu, jeu en cours, game over et victoire
- **Mécaniques classiques** : Power pellets qui rendent les fantômes vulnérables

## Architecture du projet

Le projet est organisé selon les principes de programmation orientée objet :

```plaintext
2025A-PR02-SOLUTION/
├── main.py              # Fichier à executer pour lancer le jeu
├── game.py              # Classe principale Game et boucle de jeu
├── constants.py         # Constantes et configuration du jeu
├── game_object.py       # Classe abstraite GameObject
├── pacman.py            # Classe Pacman (joueur)
├── ghost.py             # Classes des fantômes
├── maze.py              # Classe Maze (labyrinthe) et gestion des collisions
├── collectibles.py      # Classes des collectibles (Dot, PowerPellet)
└── imgs/                # Images
```

Détails des fichiers :
- `main.py` : Point d'entrée du jeu, initialise Pygame et lance la boucle principale
- `game.py` : Contient la classe `Game` qui gère la logique principale du jeu, les états des différents objets, leurs interactions ainsi que la boucle de jeu et la gestion des événements.
- `constants.py` : Définit les constantes et la configuration du jeu 
- `game_object.py` : Définit une classe abstraite `GameObject` servant de classe parent pour tous les objets du jeu
- `pacman.py` : Contient la classe `Pacman` qui gère le comportement ainsi que les animations de Pacman
- `ghost.py` : Contient les classes des différents fantômes avec leurs comportements spécifiques (RedGhost, PinkGhost, BlueGhost, OrangeGhost). La classe `Ghost` sert de classe parent pour tous les fantômes.
- `maze.py` : Contient la classe `Maze` qui gère le labyrinthe ainsi que la détection des collisions
- `collectibles.py` : Contient les classes des collectibles (Dot, PowerPellet)

## Quelques concepts de programmation orientée objet

### 1. Héritage
- **Classe parente** : `GameObject` définit l'interface commune pour tous les objets du jeu
- **Classes filles** : `Pacman`, `Ghost`, `Dot`, `PowerPellet` héritent de `GameObject`
- **Héritage multiple** : Les différents types de fantômes héritent de la classe `Ghost`

### 2. Polymorphisme
- Toutes les classes d'objets implémentent les méthodes `update()` et `draw()`
- Le code peut traiter tous les objets de manière uniforme
- Chaque classe a sa propre implémentation et donc son propre fonctionnement 
- Redéfinir une méthode de la classe parente dans une classe fille pour adapter son comportement est appelé **surcharge** (overriding)

### 3. Encapsulation
- Chaque classe gère ses propres attributs et méthodes
- Les données sont protégées et accessibles via des méthodes publiques (getters/setters)
- État interne des objets bien encapsulé

## Travail à réaliser

### Partie 1 : Gestion de Pacman (6 points)

#### 1.1 Implémenter la gestion des touches (1 point)


Vous devrez utiliser `pygame.K_RIGHT`, `pygame.K_DOWN`, `pygame.K_LEFT`, `pygame.K_UP` pour reconnaitre les touches appuyées.

#### 1.2 Implémenter le déplacement de Pacman (2 point)

Maintenant, modifiez la méthode `get_next_position` de la classe `Pacman` renvoyant:
- les nouvelles coordonnées de Pacman 
- sa hitbox à ces coordonnées (rectangle pygame permettant de détecter les collisions) 

Vous devrez utiliser les attributs `self.next_direction`, `self.x`, `self.y` et `self.speed` afin de déterminer les nouvelles coordonnées de Pacman.

#### 1.3 Implémenter les animations de Pacman (3 points)

Dans cette partie, vous devrez modifier la méthode `draw` de la classe `Pacman`. Cette méthode est appelée à chaque iteration du jeu et a pour but de mettre à jour l'animation de pacman.

Vous devrez tout d'abord utiliser l'attribut `self.mouth_open` (booléen) pour savoir si la bouche de pacman est ouverte ou fermée:
- Si la bouche est fermée, vous devrez dessiner un cercle plein jaune représentant pacman en utilisant la fonction `pygame.draw.circle`.
- Si la bouche est ouverte, vous devrez utiliser la fonction `pygame.draw.polygon` pour construire un polygone représentant pacman avec la bouche ouverte.

La fonction `pygame.draw.polygon` prend en paramètre une liste de points successif fabricant une surface fermée. Vous devrez donc calculer les coordonnées de ces points en fonction de la direction de pacman (attribut `self.direction`).

<img src="imgs/pacman_polygone.png" width="400" height="400">

> L'image ci-dessus illustre les points à calculer pour dessiner pacman avec la bouche ouverte (direction droite). Pour constituer le cercle, vous pouvez séparer les points le composant d'un angle de 5 degrés.

Ajoutez également un oeil à pacman en utilisant la fonction `pygame.draw.circle` pour dessiner un petit cercle noir. La position de cet oeil dépendra également de la direction de pacman.

### Partie 2 : Gestion des fantômes (8 points)

#### 2.1 Implémenter le déplacement des fantômes (0.5 points)

Comme dans la partie 1.2, vous devrez modifier la méthode `get_next_position` de la classe `Ghost` renvoyant:
- les nouvelles coordonnées du fantôme 
- sa hitbox à ces coordonnées (rectangle pygame permettant de détecter les collisions)

Vous devrez utiliser les attributs `self.direction`, `self.x`, `self.y` et `self.speed` afin de déterminer les nouvelles coordonnées du fantôme.

#### 2.2 Implémenter les animations des fantômes (1.5 points)

Cette fois-ci, fini la géométrie, les fantômes sont animés à l'aide d'images PNG. Vous devrez modifier la méthode `draw` de la classe `Ghost` pour afficher l'image correcte du fantôme.
Dans leur état normal (`self.vulnerable == False`) afficher l'image du fantôme correspondant à sa couleur (`self.color`). Dans leur état vulnérable (`self.vulnerable == True`), afficher l'image du fantôme affaibli (`imgs/weak_ghost.png`).

> Utiliser la fonction `pygame.image.load` pour charger une image, la fonction `pygame.transform.scale` pour redimensionner l'image et `screen.blit` pour afficher l'image sur l'écran.

Ensuite afin de simuler une animation de marche (ils ont quand même de belles chaussures), vous devrez appliquer une rotation de 10 degrés (+ ou -) en vous basant sur l'état de la variable `self.step` (`right` ou `left`). À vous de déterminer la fonction pygame la plus appropriée pour effectuer cette rotation.

Enfin, afin de s'assurer que le fantome regarde dans la direction dans laquelle il se déplace, utiliser la variable `self.last_RL_direction` pour déterminer l'orientation de l'image (droite ou gauche). À vous de déterminer la fonction pygame la plus appropriée pour changer cette orientation.

#### 2.3 Implémenter le comportement des fantômes (6 points)

La couleur des fantômes définit leur comportement. Vous devrez modifier les différentes classes RedGhost, PinkGhost, BlueGhost et OrangeGhost héritant de `Ghost` afin d'implémenter ces différents comportements.

1. **RedGhost** - Le chasseur aggressif (2 points)
- État normal: Cherche à minimiser sa distance avec Pacman
Modifier la méthode `chase_pacman` de manière à minimiser la plus grande distance avec Pacman suivant x ou y. En cas de collision avec un mur, déplacer le fantôme dans une direction aléatoire.

> Ne pas essayer de minimiser la plus grande distance (imaginons x) puis la plus petite (imaginons y). Essayer juste de minimiser la plus grande distance, en cas de collision, déplacer le fantôme dans une direction aléatoire.

- État vulnérable: Cherche à maximiser sa distance avec Pacman
Modifier la méthode `flee_from_pacman` de manière à maximiser la plus grande distance avec Pacman suivant x ou y.

2. **PinkGhost** - Le chasseur fourbe (2 points)
- État normal: Cherche à anticiper les mouvements de Pacman
Modifier la méthode `ambush_pacman` de manière à ce que le fantôme se positionne devant Pacman. Cette coordonnée objectif correspond à la position de pacman plus la moitié de la distance entre Pacman et le fantôme.

- État vulnérable: Se déplace dans une direction aléatoire (cette direction est mise à jour à chaque collision avec un mur)

3. **BlueGhost** - Le garde (1 point)
- État normal et vulnérable: Patrouille dans une direction aléatoire, sa direction est mise à jour à chaque collision avec un mur et à chaque fois que la variable `self.patrol_timer` atteint la valeur de `self.patrol_duration`. 

Modifiez ici la méthode `move` de manière à implémenter ce comportement.

4. **OrangeGhost** - Le fou (1 point)
- État normal: Son comportement varie entre deux types suivant la valeur de `self.chase_mode` (booléen):
    - Si `self.chase_mode == True`, il chasse Pacman comme le RedGhost
    - Si `self.chase_mode == False`, il se déplace dans une direction aléatoire (cette direction est mise à jour à chaque collision avec un mur)
    - La variable `self.chase_mode` est inversée à chaque fois que `self.behavior_timer` atteint la valeur de `self.behavior_duration`.

- État vulnérable: Cherche à maximiser sa distance avec Pacman, comme le RedGhost.

Modifiez ici la méthode `move` de manière à implémenter ce comportement.

> OrangeGhost hérite ici de RedGhost, pensez à ce que cela implique.

### Partie 3 : Gestion des collisions avec les murs (2 points)

Dans la classe `Maze`, vous devrez modifier la méthode `is_wall_collision` qui prend en argument un rectangle pygame (hitbox) et renvoie `True` si ce rectangle entre en collision avec un mur du labyrinthe, `False` sinon.

Pour cela, déterminer une grille 3x3 correspondant aux cases du labyrinthe proches du centre de la hitbox d'entrée et vérifier pour chacunes d'elles, s'il s'agit d'un mur (valeur 1), s'il y a collision avec la hitbox d'entrée. Les murs ont une largeur égale à `self.cell_width` et une hauteur égale à `self.cell_height`. Utiliser la méthode `pygame.Rect.colliderect` pour détecter une collision entre deux rectangles.

> Utiliser l'attribut `self.layout` pour savoir s'il s'agit d'un mur ou non.

<img src="imgs/hitbox_scheme.png" width="400" height="400">

### Partie 4 : Recherche (4 points)

**Programmer ne résume pas à compléter des fonctions à trous. Pour cette raison, cette partie fera appel à votre compréhension globale du code et à votre capacité à l'adapter. Votre objectif sera de venir intégrer dans le jeu deux portails de téléportation permettant à Pacman et aux fantômes de se téléporter d'un côté à l'autre du labyrinthe. Ces portails devront être représentés visuellement (un devra être orange et l'autre bleu) et devront être positionnés aléatoirement dans le labyrinthe sur le chemin (valeur 0 dans `self.layout`). Entrer dans le portail orange téléportera le joueur dans le portail bleu et vice-versa.
**
> Concernant l'aspect visuel, vous êtes libre d'utiliser des PNGs ou de dessiner des formes géométriques avec pygame.

> ⚠️ Pour conserver les points des autres parties, il faudra vous assurer que vos ajouts ne perturbent pas le fonctionnement actuel du jeu. Une bonne utilisation de git est alors recommandée.

Pour faciliter la correction, vous devrez également créer un fichier `RECHERCHE.md` dans lequel vous expliquerez votre démarche, les choix que vous avez faits et les difficultés que vous avez rencontrées lors de cette intégration.

### Barème de notation

Le barème de correction est le suivant : 

| **Partie**                                | **Tâche**                                                                 | **Points** |
|-------------------------------------------|---------------------------------------------------------------------------|------------|
| **Partie 1 : Gestion de Pacman** |                                                                           | **/6**     |
|      Implémenter la gestion des touches            | 1.1 | 1          |
|      Implémenter le déplacement de Pacman            | 1.2  | 2          |
|      Implémenter les animations de Pacman            | 1.3  | 3          |
| **Partie 2 : Gestion des fantômes** |                                                               | **/8**     |
|      Implémenter le déplacement des fantômes          | 2.1 | 0.5          |
|      Implémenter les animations des fantômes          | 2.2 | 1.5          |
|      Implémenter le comportement des fantômes          | 2.3 | 6          |
| **Partie 3 : Gestion des collisions avec les murs** |                                                                    | **/2**     |
|      Extraire la grille des cases proches         | 3.1 | 1          |
|      Gérer les collisions avec les murs           | 3.2 | 1          |
| **Partie 4 : Recherche** |                                                                    | **/4**     |
|      Le raisonnement est bon dans le fichier `RECHERCHE.md`             | 4.1 | 1.5          |
|      Les portails sont correctement implémentés             | 4.2 | 2.5          |
| **Total**                                 |                                                                           | **/20**    |















