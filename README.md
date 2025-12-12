# Challenge Triple A — Dashboard de Monitoring

## Sommaire
- [ Description](#-description)
- [Prérequis](#prérequis)
- [Installation](#-installation)
- [Installation des dépendances](#️-installation-des-dépendances)
- [Utilisation](#-utilisation)
  - [Lancer le script](#️-lancer-le-script)
  - [Ouvrir le dashboard](#-ouvrir-le-dashboard)
- [Fonctionnalités](#-fonctionnalités)
- [Captures d'écran](#️-captures-décran)
- [Difficultés rencontrées](#-difficultés-rencontrées)
- [Améliorations possibles](#-améliorations-possibles)
- [Auteurs](#-auteurs)

---

## Description
Ce projet consiste à créer un **dashboard de monitoring système** généré automatiquement via un script Python.  
Le script récupère diverses informations (CPU, RAM, uptime, processus...) et génère une page HTML statique à l’aide d’un template **Jinja2**.

---

## Prérequis
- **Python 3.8+**
- Modules Python :
  - `psutil`
  - `flask`
  - `jinja2`

---

## Installation
Clonez le projet :

```bash
git clone https://github.com/logann-grange/AAA
cd AAA
```

---

## Installation des dépendances

```bash
pip install psutil jinja2
```

---

## Utilisation

### Lancer le script

```bash
python3 monitor.py
```

---

### Ouvrir le dashboard
Ouvrez simplement le fichier :

- Double-cliquez sur `template.html`, **ou**
- Utilisez :

```bash
xdg-open template.html   # Linux
open template.html       # macOS
start template.html      # Windows
```

La page se mettra à jour toutes les 30 secondes.

---

## Fonctionnalités
### Informations système
- Nom de la machine
- Système d’exploitation (OS)
- Architecture
- Uptime complet (jours, heures, minutes)
- Nombre d’utilisateurs connectés
- Adresse IP principale
- Heure de démarrage de la machine
- Charge système : Load 1 min / 5 min / 15 min

### CPU
- Nom / modèle du processeur
- Fréquence actuelle en MHz
- Nombre de cœurs logiques
- Utilisation CPU globale (jauge en demi-cercle Canvas)
- Utilisation CPU par cœur (mini-jauges dynamiques Canvas)
- Couleur automatique selon la charge (vert / orange / rouge)

### RAM
- RAM totale
- RAM utilisée (Go)
- Pourcentage d’utilisation
- Jauge RAM dynamique en Canvas
- Indicateur coloré selon le niveau de charge

### Processus
- Top 3 processus les plus gourmands en CPU
- Top 3 processus les plus gourmands en RAM
- Affichage CPU% et RAM% pour chaque processus

### Analyse des fichiers
- Analyse récursive du dossier Documents
- Comptage des fichiers par type :
.txt, .py, .pdf, .jpg, .html, .png, .css, .mp3, .mp4, .zip
- Calcul du pourcentage par extension
- Conversion automatique des tailles (Ko, Mo, Go...)
- Top 5 des fichiers les plus volumineux
- Affichage du chemin complet + taille humaine pour chaque fichier

### Interface et affichage
- Génération HTML via Flask + Jinja2
- Rafraîchissement automatique de la page toutes les 30 secondes
- Jauges visuelles Canvas (CPU + RAM + cœurs)
- Design responsive
- Affichage d’icônes informatives
- Mise en page structurée en sections

### Techniques
- Application web générée avec Flask
- Récupération des données système avec psutil
- Parcours de fichiers avec gestion des permissions
- Utilisation de tojson pour transférer les données Python → JavaScript
- Ouverture automatique du navigateur
- Code modulaire et organisé (fonctions séparées : CPU, RAM, fichiers, processus…)
- Design responsive  


---

## Captures d'écran
Header :
<img width="1881" height="235" alt="image" src="https://github.com/user-attachments/assets/26332441-8955-4109-b220-30aedd317d32" />
Body :
<img width="1865" height="973" alt="image" src="https://github.com/user-attachments/assets/a04b9260-096b-4afe-b183-9d5291e6039f" />
<img width="1858" height="908" alt="image" src="https://github.com/user-attachments/assets/9baf696b-3e5d-4a09-856f-f3de0a7bae76" />
<img width="1862" height="571" alt="image" src="https://github.com/user-attachments/assets/08723136-ba4e-4bc5-9d54-12f71cfacf98" />
Footer :
<img width="1871" height="111" alt="image" src="https://github.com/user-attachments/assets/44534202-331b-46b7-a308-21f23f8bae5f" />


---

## Difficultés rencontrées
- Problèmes réseau de la VM 
- Création des jauges

---

## Améliorations possibles
- Mode sombre vs mode clair
- Changement des couleurs vert / rouge pour une meilleure accecssibilité (daltonisme)
- Interface interactive (recherche, filtres)
- Navigation multi-onglets (CPU / RAM / Processus / Réseau)
- Ajout d’un onglet "Réseau" (débit entrant/sortant)

---

## Auteurs
- **Logann**
- **Anna** 
