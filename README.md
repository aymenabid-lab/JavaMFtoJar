# 🧩 JavaMFtoJar  
### A web-based tool for compiling Java ME (J2ME) applications into `.jar` files

[🔗 GitHub Repository](https://github.com/aymenabid-lab/JavaMFtoJar)

---

## 🚀 Description

**JavaMFtoJar** est une application web légère développée avec **Flask (Python)**  
et déployée dans l’environnement de développement en ligne **[Replit – JarCompiler](https://replit.com/@aymenabid/JarCompiler)**.  

Elle permet de **compiler des projets Java ME (J2ME)** directement depuis le navigateur,  
en générant automatiquement un fichier `.jar` exécutable à partir des sources `.java` et du fichier `manifest.mf`.  

Ce projet vise à moderniser et simplifier la compilation de MIDlets,  
en offrant une solution web accessible sans installation locale de SDK Java ME.

---

## ⚙️ Installation

### 1️⃣ Installer Flask

Si le message d’erreur indique que **Flask n’est pas installé**,  
ouvre un terminal et exécute la commande suivante :

```bash
pip3 install flask







Parfait ✅ voici la **version finale complète du `README.md`**, avec tout ton contenu intégré, la description mise à jour, la section sur Flask, et l’ajout de la **capture d’écran `interface.jpg`** en bas.
Tu peux copier-coller directement ce texte dans ton fichier **`README.md`** sur GitHub :

---

````markdown
# 🧩 JavaMFtoJar  
### A web-based tool for compiling Java ME (J2ME) applications into `.jar` files

[🔗 GitHub Repository](https://github.com/aymenabid-lab/JavaMFtoJar)

---

## 🚀 Description

**JavaMFtoJar** est une application web légère développée avec **Flask (Python)**  
et déployée dans l’environnement de développement en ligne **[Replit – JarCompiler](https://replit.com/@aymenabid/JarCompiler)**.  

Elle permet de **compiler des projets Java ME (J2ME)** directement depuis le navigateur,  
en générant automatiquement un fichier `.jar` exécutable à partir des sources `.java` et du fichier `manifest.mf`.  

Ce projet vise à moderniser et simplifier la compilation de MIDlets,  
en offrant une solution web accessible sans installation locale de SDK Java ME.

---

## ⚙️ Installation

### 1️⃣ Installer Flask

Si le message d’erreur indique que **Flask n’est pas installé**,  
ouvre un terminal et exécute la commande suivante :

```bash
pip3 install flask
````

> 💡 Si tu utilises un environnement virtuel (`venv`), active-le avant d’installer Flask.

---

### 2️⃣ Vérifier l’installation

Pour t’assurer que Flask est bien installé :

```bash
python3 -m pip show flask
```

Tu devrais voir apparaître les informations sur le package (nom, version, chemin, etc.).

---

### 3️⃣ Lancer l’application

Une fois Flask installé, exécute simplement :

```bash
python3 app.py
```

Puis ouvre ton navigateur et accède à :

```
http://127.0.0.1:5000
```

L’interface web de **JavaMFtoJar** s’ouvrira pour te permettre de charger et compiler ton projet.

---

## 🧠 Astuce – Utiliser un environnement virtuel

Pour éviter tout conflit entre dépendances, tu peux créer un environnement virtuel dédié :

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
python app.py
```

> Sous Windows :
>
> ```bash
> venv\Scripts\activate
> ```

---

## 🧰 Technologies utilisées

* 🐍 **Python 3.x**
* 🌐 **Flask** — Framework web léger
* ☕ **Java ME (J2ME)** — Compilation des MIDlets
* 📦 **JAR Packaging** — Génération automatique d’archives `.jar`
* 💻 **Replit Environment** — Développement et hébergement du compilateur web

---

## 👨‍💻 Auteur

**Dr. Aymen ABID**
📧 [aymen.abid@enis.tn](mailto:aymen.abid@enis.tn)
🏫 ESPIN – École Supérieure Privée d'Ingénierie et de Technologies Numériques
🧩 Master Ingénierie des Systèmes Embarqués – 2025/2026

---

## 📄 Licence

Ce projet est distribué sous licence **MIT**.
Vous êtes libre de l’utiliser, le modifier et le redistribuer à des fins éducatives ou de recherche.

---

## 🖼️ Aperçu de l’interface

Voici un aperçu de l’interface web de **JavaMFtoJar** (version Replit) :

![Interface JavaMFtoJar](interface.jpg)

> *L’interface permet de choisir un fichier `.zip` contenant les sources du projet Java ME
> et de générer automatiquement un fichier `.jar` exécutable directement téléchargeable.*

```

---

💡 Tu peux placer ton image `interface.jpg` à la racine du dépôt GitHub (même dossier que `README.md`),  
et GitHub l’affichera automatiquement sous la section **“Aperçu de l’interface”**.  

Souhaites-tu que je te crée aussi une **capture d’écran simulée** propre (interface claire avec boutons “Choose file” et “Compile JAR”) à inclure comme `interface.jpg` ?
```
