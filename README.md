# 🔧 Challenge Triple A — Dashboard de Monitoring

## 📑 Sommaire
- [📘 Description](#-description)
- [🧰 Prérequis](#-prérequis)
- [📦 Installation](#-installation)
- [⚙️ Installation des dépendances](#️-installation-des-dépendances)
- [🚀 Utilisation](#-utilisation)
- [▶️ Lancer le script](#️-lancer-le-script)
- [🌐 Ouvrir le dashboard](#-ouvrir-le-dashboard)
- [✨ Fonctionnalités](#-fonctionnalités)
- [🖼️ Captures d'écran](#-captures-décran)
- [🐞 Difficultés rencontrées](#-difficultés-rencontrées)
- [🚧 Améliorations possibles](#-améliorations-possibles)
- [👥 Auteurs](#-auteurs)


## 📘 Description
Ce projet consiste à créer un **dashboard de monitoring système** généré automatiquement via un script Python.  
Le script récupère différentes informations liées au système (CPU, RAM, uptime, processus, etc.) et génère une page HTML statique grâce à un template **Jinja2**.

Le résultat final est un fichier **`index.html`**, affichant un tableau de bord mis à jour automatiquement toutes les 30 secondes.


## 🧰 Prérequis
Avant d’exécuter le script, assurez-vous de disposer de :

- **Python 3.8+**
- Modules Python requis :
  - `psutil`
  - `jinja2`


## 📦 Installation
Clonez le projet depuis GitHub :

```bash
git clone https://github.com/logann-grange/AAA
cd AAA```

# ⚙️ Installation des dépendances
Installez les modules nécessaires via pip :
pip install psutil jinja2

## 🚀 Utilisation

# ▶️ Lancer le script
Exécutez :
python3 monitor.py

Un fichier index.html sera généré dans le dossier du projet.

# 🌐 Ouvrir le dashboard
Pour afficher le dashboard :
    Double-cliquez sur index.html
    ou utilisez l’une des commandes selon votre OS :
xdg-open index.html   # Linux
open index.html       # macOS
start index.html      # Windows

La page se rafraîchira automatiquement toutes les 30 secondes grâce à la balise meta-refresh.

## ✨ Fonctionnalités
🖥️ Informations système
    Nom de la machine
    OS et architecture
    Uptime détaillé
    Utilisateurs connectés
    Adresse IP

⚙️ Informations CPU
    Nom / modèle
    Fréquence actuelle
    Nombre de cœurs
    Utilisation en temps réel avec barre de progression

🧠 Informations RAM
    RAM totale
    RAM utilisée
    Pourcentage d'utilisation

📊 Processus
    Top 3 des processus les plus gourmands en CPU
    Top 3 des processus les plus gourmands en RAM

🛠️ Techniques
    Génération automatique d’un fichier HTML propre et lisible
    Rafraîchissement automatique toutes les 30 secondes
    Design simple et responsive

##🖼️ Captures d'écran


## 🐞 Difficultés rencontrées
    - Connexion internet de la VM ("initialisation des réseaux virutels")
    - 
    

## 🚧 Améliorations possibles
    - Ajout d’un mode sombre
    - Graphiques en temps réel (Chart.js ou équivalent)
    - Service systemd pour une génération automatique
    - Interface interactive (filtres, recherche, tri dynamique)
    - Organisation en onglets (CPU / RAM / Processus / Réseau)

# 👥 Auteurs
    - Gaïa — CSS
    - Logann — Script Python
    - Anna — Structure HTML
