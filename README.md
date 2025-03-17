# 🌟 Simulateur de Créature Virtuelle 🌟

Un simulateur de créature virtuelle complet inspiré des Tamagotchis, entièrement développé en Python. Ce projet vous permet d'élever, de nourrir et de prendre soin de différentes créatures virtuelles dans un environnement interactif riche en fonctionnalités.

## 📋 Table des matières
- [Introduction](#-introduction)
- [Caractéristiques principales](#-caractéristiques-principales)
- [Types de créatures](#-types-de-créatures)
- [Personnalisation](#-personnalisation)
- [Attributs et statistiques](#-attributs-et-statistiques)
- [Cycle de vie](#-cycle-de-vie)
- [Système météorologique](#-système-météorologique)
- [Mini-jeux](#-mini-jeux)
- [Événements aléatoires](#-événements-aléatoires)
- [Système social](#-système-social)
- [Inventaire et objets](#-inventaire-et-objets)
- [Boutique](#-boutique)
- [Actions disponibles](#-actions-disponibles)
- [Interface utilisateur](#-interface-utilisateur)
- [Système de sauvegarde](#-système-de-sauvegarde)
- [Architecture technique](#-architecture-technique)
- [Installation et exécution](#-installation-et-exécution)
- [Dépendances](#-dépendances)
- [Crédits et remerciements](#-crédits-et-remerciements)
- [Licence](#-licence)
- [Message final](#-message-final)

## 🎮 Introduction

Le Simulateur de Créature Virtuelle est un jeu en ligne de commande qui vous plonge dans l'expérience nostalgique d'élever un compagnon virtuel. À la différence des Tamagotchis traditionnels, ce simulateur propose un grand nombre de fonctionnalités avancées comme un système météorologique dynamique, des mini-jeux interactifs, un système social, et bien plus encore.

Chaque créature possède des caractéristiques uniques, des préférences, et un cycle de vie complet. Votre rôle est de veiller à son bien-être en maintenant ses différentes jauges (faim, énergie, bonheur, santé) à des niveaux optimaux, tout en l'aidant à évoluer et à s'épanouir dans son environnement virtuel.

## ✨ Caractéristiques principales

- **Simulation complète** : Cycle jour/nuit, vieillissement, évolution, et mort éventuelle
- **Variété de créatures** : 5 types différents avec des attributs spécifiques
- **Personnalisation poussée** : Couleurs et traits de caractère affectant le gameplay
- **Système météorologique** : 7 types de temps influençant l'humeur de votre créature
- **Mini-jeux interactifs** : 3 jeux différents avec des récompenses
- **Événements aléatoires** : Plus de 15 événements possibles lors de l'exploration
- **Système social** : Interactions avec d'autres créatures, création de liens d'amitié
- **Interface colorée** : Utilisation d'emojis et de couleurs ANSI pour une meilleure immersion
- **Système de sauvegarde** : Possibilité de sauvegarder et de charger votre progression

## 🐾 Types de créatures

Le jeu propose 5 types de créatures différentes, chacune avec ses caractéristiques uniques :

| Type | Emoji | Caractéristiques |
|------|-------|------------------|
| **Chaton** | 🐱 | Consomme plus de nourriture (+20%), utilise moins d'énergie (-10%), bonheur légèrement accru (+10%) |
| **Chiot** | 🐶 | Consomme beaucoup de nourriture (+30%), utilise plus d'énergie (+20%), bonheur fortement accru (+30%) |
| **Dragon** | 🐉 | Très gourmand (+50%), économe en énergie (-20%), bonheur légèrement réduit (-10%) |
| **Robot** | 🤖 | Consomme peu de nourriture (-30%), utilise beaucoup d'énergie (+40%), bonheur réduit (-20%) |
| **Lapin** | 🐰 | Consommation de nourriture modérée (+10%), utilisation d'énergie modérée (+10%), bonheur accru (+20%) |

Chaque type a également un événement spécial qui lui est propre :
- 🐱 **Chaton** : Peut chasser une souris imaginaire (bonus de bonheur, perte d'énergie)
- 🐶 **Chiot** : Peut enterrer un trésor dans le jardin (bonus de bonheur, perte d'énergie)
- 🐉 **Dragon** : Peut cracher une petite flamme (bonus de bonheur, perte d'énergie)
- 🤖 **Robot** : Peut recevoir une mise à jour (gain d'énergie et de bonheur)
- 🐰 **Lapin** : Peut grignoter une carotte (gain de satiété et de bonheur)

## 🎨 Personnalisation

### Couleurs disponibles
Chaque type de créature propose plusieurs options de couleur :

- 🐱 **Chaton** : gris, roux, blanc, noir, tigré, standard
- 🐶 **Chiot** : marron, blanc, noir, tacheté, standard
- 🐉 **Dragon** : rouge, vert, bleu, noir, doré, standard
- 🤖 **Robot** : argent, or, bleu, noir, rouge, standard
- 🐰 **Lapin** : blanc, gris, marron, noir, roux, standard

### Traits de caractère
Les traits influencent significativement les statistiques et le comportement de votre créature :

| Trait | Emoji | Effets |
|-------|-------|--------|
| **Normal** | 😊 | Aucun bonus ou malus particulier |
| **Joueur** | 🎯 | +10 bonheur, -5 énergie |
| **Gourmand** | 🍽️ | -10 faim, -5 santé |
| **Sportif** | 🏃 | +10 énergie, -5 faim |
| **Paresseux** | 😴 | -10 énergie, +5 bonheur |
| **Curieux** | 🔍 | +5 bonheur, +5 énergie |
| **Timide** | 🙈 | -5 bonheur, -20 niveau social |
| **Sociable** | 👋 | +5 bonheur, +20 niveau social |
| **Intelligent** | 🧠 | +10 points de jeu, avantage dans les mini-jeux |

## 📊 Attributs et statistiques

Votre créature possède plusieurs attributs que vous devez surveiller et maintenir :

- 🍔 **Faim** (0-100) : Représente le niveau de satiété. Si la faim tombe trop bas (<20), la santé diminue.
- ⚡ **Énergie** (0-100) : Représente la vitalité. Si l'énergie est trop basse (<20), le bonheur diminue.
- 😊 **Bonheur** (0-100) : Représente l'humeur. Un bonheur élevé est essentiel pour une créature épanouie.
- ❤️ **Santé** (0-100) : Représente l'état de santé général. Si elle atteint 0, la créature meurt.
- 👋 **Niveau social** (0-100) : Représente la sociabilité. Augmente en rencontrant d'autres créatures.
- 🧪 **État de maladie** : Indique si la créature est malade (nécessite des soins).
- 💰 **Points de jeu** : Monnaie obtenue en jouant aux mini-jeux, utilisable dans la boutique.

Tous ces attributs évoluent avec le temps et sont influencés par vos actions et les événements aléatoires.

## 🌱 Cycle de vie

Votre créature traverse trois stades d'évolution au cours de sa vie :

1. 👶 **Bébé** (0-30 jours) : État initial, vulnérable mais adorable
2. 👦 **Jeune** (30-60 jours) : Plus résistant, avec une personnalité qui se développe
3. 🧑 **Adulte** (60+ jours) : Pleinement développé, avec toutes ses capacités

L'âge est calculé en jours (et heures) et augmente à chaque action que vous effectuez. Les transitions entre les stades sont marquées par des événements d'évolution spéciaux.

Si la santé de votre créature atteint 0, elle meurt malheureusement. Un message commémoratif s'affiche, indiquant l'âge atteint.

## ⛅ Système météorologique

Un système météorologique dynamique influence l'humeur de votre créature. La météo change chaque jour (en temps de jeu) et offre différents effets :

| Météo | Emoji | Effet sur le bonheur |
|-------|-------|---------------------|
| **Soleil** | ☀️ | +5% |
| **Pluie** | 🌧️ | -3% |
| **Neige** | ❄️ | +2% |
| **Orage** | ⚡ | -8% |
| **Brouillard** | 🌫️ | -2% |
| **Vent** | 💨 | -1% |
| **Canicule** | 🔥 | -10% |

La météo est mise à jour automatiquement chaque jour dans le temps du jeu et est affichée dans l'interface d'état de la créature.

## 🎲 Mini-jeux

Le simulateur propose trois mini-jeux interactifs qui vous permettent de gagner des points et parfois des objets :

### 🔢 Devinette
- **Difficulté** : Facile
- **Description** : Devinez un nombre entre 1 et 10 en 3 essais maximum
- **Récompenses** : 
  - Réussite au 1er essai : 30 points, +15 bonheur, chance de gagner une Friandise ou un Jouet
  - Réussite au 2e essai : 20 points, +15 bonheur
  - Réussite au 3e essai : 10 points, +15 bonheur
  - Échec : 0 point, +5 bonheur (petit bonus pour avoir essayé)
- **Bonus spécial** : Les créatures avec le trait "intelligent" reçoivent un indice sur la plage du nombre

### ⏱️ Réflexe
- **Difficulté** : Moyenne
- **Description** : Appuyez sur Entrée dès que vous voyez "MAINTENANT!" s'afficher
- **Récompenses** :
  - Moins de 0.5 seconde : 30 points, +20 bonheur, chance de gagner une Potion d'énergie
  - Moins de 1.0 seconde : 20 points, +15 bonheur, chance de gagner une Friandise
  - Moins de 2.0 secondes : 10 points, +10 bonheur
  - Plus de 2.0 secondes : 0 point, +5 bonheur
- **Bonus spécial** : Les créatures avec le trait "sportif" reçoivent un bonus de temps de 0.5 seconde

### 🧩 Mémoire
- **Difficulté** : Difficile
- **Description** : Mémorisez une séquence de 6 à 8 symboles et reproduisez-la
- **Récompenses** :
  - Séquence parfaite : 30-40 points, +25 bonheur, chance de gagner un Livre magique
  - Une erreur : 15-25 points, +20 bonheur, chance de gagner un Jouet
  - Moitié correcte : 6-16 points, +15 bonheur
  - Moins de la moitié : 0 point, +5 bonheur
- **Bonus spécial** : Les créatures avec le trait "intelligent" reçoivent une séquence plus longue (8 symboles au lieu de 6) mais avec des récompenses plus importantes

Jouer aux mini-jeux consomme de l'énergie (-10) et fait passer 1 heure de temps dans le jeu.

## 🌍 Événements aléatoires

En explorant, votre créature peut rencontrer plus de 15 événements aléatoires différents :

### Événements généraux (pour tous les types de créatures)
- 🧸 Trouver un jouet (+10 bonheur)
- 😠 Se disputer avec une autre créature (-5 bonheur)
- 🍽️ Manger un bon repas (+10 faim, +5 bonheur)
- 🎨 Faire un dessin (+8 bonheur)
- 🌧️ Rester à l'intérieur à cause de la pluie (+5 énergie, -3 bonheur)
- ☀️ Profiter du beau temps (+7 bonheur, -3 énergie)
- 💤 Faire une sieste imprévue (+15 énergie, -5 faim)
- 😱 Avoir peur d'un bruit fort (-8 bonheur, -5 énergie)
- 🍬 Recevoir une friandise d'un visiteur (+8 faim, +5 bonheur)
- 😣 Trébucher et se faire mal (-5 bonheur, -10 énergie)
- 🦠 Attraper le covid-19 (-10 bonheur, -15 énergie, -20 santé)
- 💦 Essayer d'apprendre à nager et se noyer (-15 bonheur, -20 énergie, -30 santé)
- 🤢 Mal digérer un aliment (-5 bonheur, -8 énergie, -10 santé)
- 🎁 Recevoir un cadeau inattendu (+15 bonheur)

### Événements spécifiques (selon le type de créature)
- 🐱 **Chaton** : Chasser une souris imaginaire (+10 bonheur, -8 énergie)
- 🐶 **Chiot** : Enterrer un trésor dans le jardin (+12 bonheur, -10 énergie)
- 🐉 **Dragon** : Cracher une petite flamme (+15 bonheur, -12 énergie)
- 🤖 **Robot** : Recevoir une mise à jour (+20 énergie, +8 bonheur)
- 🐰 **Lapin** : Grignoter une carotte (+15 faim, +8 bonheur)

Explorer prend 30 minutes de temps dans le jeu et peut également déclencher un changement de météo si un jour entier s'est écoulé.

## 👫 Système social

Votre créature peut rencontrer d'autres créatures et développer des relations sociales :

- **Rencontres programmées** : Vous pouvez choisir le type et le nom de la créature à rencontrer
- **Rencontres aléatoires** : Le jeu peut sélectionner aléatoirement une créature à rencontrer

### Types de rencontres possibles
- 👫 Devenir amis (+15 bonheur, ajout à la liste d'amis)
- 😠 Ne pas s'entendre (-5 bonheur)
- 🍽️ Partager de la nourriture (+8 bonheur, -10 faim)
- 🎮 Apprendre un nouveau jeu (+12 bonheur)
- 👻 Se faire effrayer par une farce (-8 bonheur)
- 🧭 Aider l'autre créature à retrouver son chemin (+10 bonheur)
- 😠 Se faire voler un jouet (-5 bonheur)
- 🎯 Jouer ensemble (+10 bonheur)
- 🍽️ Partager un repas (+12 bonheur, +10 faim)
- 💤 Faire une sieste ensemble (+8 bonheur, +10 énergie)
- 🎨 Dessiner ensemble (+10 bonheur)

Rencontrer une créature prend 30 minutes de temps dans le jeu et augmente le niveau social de votre créature, surtout si la rencontre est positive.

## 🎒 Inventaire et objets

Votre créature peut acquérir, stocker et utiliser divers objets qui affectent ses statistiques :

| Objet | Emoji | Effets | Source | Prix |
|-------|-------|--------|--------|------|
| **Friandise** | 🍬 | +15 faim, +5 bonheur | Mini-jeux, boutique | 10 points |
| **Jouet** | 🧸 | +15 bonheur, -5 énergie | Mini-jeux, boutique | 15 points |
| **Potion d'énergie** | ⚡ | +30 énergie | Mini-jeux, boutique | 20 points |
| **Potion de santé** | 💊 | +30 santé, guérit la maladie | Mini-jeux, boutique | 25 points |
| **Amulette de protection** | 🔮 | +10 santé (permanent) | Boutique | 50 points |
| **Livre magique** | 📚 | +10 bonheur, +5 points de jeu (permanent) | Mini-jeux, boutique | 40 points |

Les objets permanents (Amulette et Livre) ne sont pas consommés après utilisation et continuent à fournir leurs bonus.

Utiliser un objet prend 15 minutes de temps dans le jeu.

## 🛒 Boutique

La boutique vous permet de dépenser vos points de jeu pour acheter des objets utiles :

- Points de jeu : Gagnés principalement via les mini-jeux
- Variété d'objets : Des objets consommables aux objets permanents offrant des bonus durables
- Interface dédiée : Affiche clairement les prix et les effets de chaque objet

Le catalogue complet est accessible via le menu "Boutique" et indique le prix et la description de chaque article.

## 🎮 Actions disponibles

Votre créature peut effectuer de nombreuses actions, chacune consommant du temps de jeu :

### 🍕 Nourrir
- **Types de nourriture** :
  - **Standard** : +20 faim (modifié par le multiplicateur de type)
  - **Premium** : +30 faim, +5 bonheur (modifié par le multiplicateur de type)
  - **Malsaine** : +15 faim, -5 santé (modifié par le multiplicateur de type)
- **Temps consommé** : Instantané

### 🎯 Jouer
- **Effets** : +15 bonheur par heure (modifié par le multiplicateur de type), -10 énergie par heure, -5 faim par heure
- **Temps consommé** : Durée spécifiée (en heures)
- **Restrictions** : Nécessite au moins 20 points d'énergie

### 💤 Dormir
- **Effets** : +10 énergie par heure (modifié par le multiplicateur de type), -5 faim par heure
- **Temps consommé** : Durée spécifiée (en heures)

### 🏥 Soigner
- **Effets** : Guérit la maladie si présente, +30 santé
- **Temps consommé** : Instantané

### 🌍 Explorer
- **Effets** : Déclenche un événement aléatoire
- **Temps consommé** : 30 minutes

### 👋 Rencontrer une créature
- **Effets** : Déclenche une interaction sociale qui peut affecter le bonheur, l'énergie, la faim et le niveau social
- **Temps consommé** : 30 minutes

### 🎲 Jouer à un mini-jeu
- **Effets** : Permet de gagner des points de jeu et des objets, -10 énergie
- **Temps consommé** : 1 heure
- **Restrictions** : Nécessite au moins 15 points d'énergie

### 🎒 Utiliser un objet
- **Effets** : Applique les effets spécifiques de l'objet
- **Temps consommé** : 15 minutes

### 💾 Sauvegarder
- **Effets** : Sauvegarde l'état actuel de la créature
- **Temps consommé** : Instantané

Toutes ces actions font également progresser le temps, ce qui affecte les attributs de la créature (diminution naturelle de la faim, de l'énergie et du bonheur).

## 💻 Interface utilisateur

L'interface en ligne de commande est enrichie par l'utilisation de couleurs ANSI et d'emojis pour une meilleure lisibilité :

### 📊 Affichage de l'état
- Barres de progression colorées pour les attributs
- Code couleur intuitif (rouge pour les alertes, vert pour la santé, etc.)
- Indication claire des états critiques
- Affichage de la météo actuelle et de ses effets
- Liste des amis et de l'inventaire

### 🚨 Alertes et notifications
- Alertes visuelles pour les états critiques (faim basse, maladie, etc.)
- Messages colorés pour les événements importants
- Signalement des transitions d'évolution

### 🎨 Personnalisation de l'affichage
- Emojis adaptés à chaque type de créature
- Couleurs différentes pour chaque type d'attribut
- Transitions visuelles lors des événements importants (évolution, mort)

## 💾 Système de sauvegarde

Le jeu utilise un système de sauvegarde complet basé sur JSON :

- **Sauvegarde** : Enregistre toutes les statistiques et l'état de la créature
- **Chargement** : Restaure exactement l'état de la créature tel qu'il était lors de la sauvegarde
- **Attributs sauvegardés** : Nom, type, couleur, trait de caractère, tous les attributs numériques, état de maladie, stade d'évolution, niveau social, liste d'amis, points de jeu, inventaire

Par défaut, le fichier de sauvegarde est nommé "sauvegarde.json", mais vous pouvez spécifier un nom différent.

## 🧱 Architecture technique

Le projet est organisé en modules bien structurés :

```
tamagotchi-python/
├── main.py                # Point d'entrée du programme
├── game/
│   ├── game_manager.py    # Gestionnaire principal du jeu
│   ├── events.py          # Gestion des événements aléatoires
│   └── mini_games.py      # Implémentation des mini-jeux
├── models/
│   └── creature.py        # Classe définissant les créatures
├── ui/
│   ├── display.py         # Fonctions d'affichage
│   └── menu.py            # Gestion des menus
└── utils/
    └── file_manager.py    # Gestion des sauvegardes
```

### 🔍 Description des modules

- **main.py** : Coordonne le flux du programme et gère la boucle principale du jeu
- **game_manager.py** : Contient la classe `Game` qui orchestrate toutes les fonctionnalités
- **events.py** : Gère la génération d'événements aléatoires et de rencontres
- **mini_games.py** : Implémente les trois mini-jeux disponibles
- **creature.py** : Définit la classe `Creature` avec tous ses attributs et méthodes
- **display.py** : Gère l'affichage formaté avec couleurs et emojis
- **menu.py** : Implémente les différents menus et interfaces utilisateur
- **file_manager.py** : Fournit les fonctions de sauvegarde et de chargement

## 🚀 Installation et exécution

### Prérequis
- Python 3.6 ou supérieur
- Système d'exploitation compatible avec les codes couleur ANSI (Windows 10+, macOS, Linux)

### Étapes d'installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/gonicolas12/tamagotchi-python.git
cd tamagotchi-python
```

2. Lancez le jeu :
```bash
python main.py
```

### Compatibilité

- **Windows** : Fonctionne correctement sur Windows 10+ avec le terminal par défaut
- **macOS/Linux** : Compatible avec tous les terminaux standards
- **Encodage** : Utilise UTF-8 pour les emojis et les caractères spéciaux

## 📦 Dépendances

Ce projet utilise uniquement la bibliothèque standard de Python, sans dépendances externes :

- **random** : Génération de nombres aléatoires pour les événements et mini-jeux
- **json** : Sauvegarde et chargement des données
- **time** : Gestion du temps dans les mini-jeux et le système de temps du jeu
- **os** : Opérations liées au système d'exploitation (effacement d'écran, vérification de fichiers)

## 🙏 Crédits et remerciements

- **Inspiration** : Les Tamagotchis originaux de Bandai (1996)
- **Emojis** : Fournis par la norme Unicode Standard
- **Codes couleur ANSI** : Standard pour les terminaux modernes

## 📜 Licence

Ce projet est distribué sous la licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 💬 Message final

Merci d'avoir exploré le Simulateur de Créature Virtuelle ! Ce projet est le fruit d'un travail passionné visant à recréer et enrichir l'expérience nostalgique des Tamagotchis. 

**Prenez bien soin de vos créatures virtuelles !** 🐾