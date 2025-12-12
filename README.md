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
- [🖼️ Captures d'écran](#️-captures-décran)
- [🐞 Difficultés rencontrées](#-difficultés-rencontrées)
- [🚧 Améliorations possibles](#-améliorations-possibles)
- [👥 Auteurs](#-auteurs)

---

## 📘 Description
Ce projet consiste à créer un **dashboard de monitoring système** généré automatiquement via un script Python.  
Le script récupère diverses informations (CPU, RAM, uptime, processus...) et génère une page HTML statique à l’aide d’un template **Jinja2**.

Le résultat final est un fichier **`index.html`** affichant un tableau de bord actualisé automatiquement toutes les 30 secondes.

---

## 🧰 Prérequis
- **Python 3.8+**
- Modules Python :
  - `psutil`
  - `flask`
  - `jinja2`

---

## 📦 Installation
Clonez le projet :

```bash
git clone https://github.com/logann-grange/AAA
cd AAA
```

---

## ⚙️ Installation des dépendances

```bash
pip install psutil jinja2
```

---

## 🚀 Utilisation

### ▶️ Lancer le script

```bash
python3 monitor.py
```

Un fichier **`index.html`** sera généré automatiquement.

---

### 🌐 Ouvrir le dashboard
Ouvrez simplement le fichier :

- Double-cliquez sur `index.html`, **ou**
- Utilisez :

```bash
xdg-open index.html   # Linux
open index.html       # macOS
start index.html      # Windows
```

La page se mettra à jour toutes les 30 secondes.

---

## ✨ Fonctionnalités

### 🖥️ Informations système
- Nom de la machine  
- OS et architecture  
- Uptime  
- Utilisateurs connectés  
- Adresse IP  

### ⚙️ CPU
- Modèle du processeur  
- Fréquence  
- Nombre de cœurs  
- Utilisation CPU (barre de progression)  

### 🧠 RAM
- RAM totale  
- RAM utilisée  
- Pourcentage d’utilisation  

### 📊 Processus
- Top 3 CPU  
- Top 3 RAM  

### 🛠️ Techniques
- Génération HTML automatique  
- Rafraîchissement auto  
- Design responsive  

---

## 🖼️ Captures d'écran


---

## 🐞 Difficultés rencontrées
- Problèmes réseau de la VM 
- création des jauges

---

## 🚧 Améliorations possibles
- Mode sombre vs mode clair
- Changement des couleurs vert / rouge pour une meilleure accecssibilité (daltonisme)
- Interface interactive (recherche, filtres)
- Navigation multi-onglets (CPU / RAM / Processus / Réseau)

---

## 👥 Auteurs
- **Logann**
- **Anna** 
