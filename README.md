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
```
**Nb.** 

 > 💡 Pré-requis: Python3 pipline
 ```bash
sudo apt install python3-pip
```
Pour l'erreur: 
<img width="550" height="47" alt="image" src="https://github.com/user-attachments/assets/393ced9b-d4b3-4cb7-8e9c-1af229beb3fc" />

> 💡 Pré-requis: javac command (Java compiler)
```bash
sudo apt install default-jdk
```
 
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
# 1. Créer un environnement virtuel
python3 -m venv venv

# 2. Activer l'environnement
source venv/bin/activate

# 3. Installer Flask dans cet environnement
pip install flask

# 4. Lancer ton application
python3 app.py

```

> Sous Windows :
>
> ```bash
> venv\Scripts\activate
> ```

---

## Installer Flask via apt (système)

>Si tu veux installer Flask pour tout le système :
>```bash
>sudo apt update
>sudo apt install python3-flask
>
>```

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

---

## 📄 Licence

Ce projet est distribué sous licence **MIT**.
Vous êtes libre de l’utiliser, le modifier et le redistribuer à des fins éducatives ou de recherche.

---

## 🖼️ Aperçu de l’interface

Voici un aperçu de l’interface web de **JavaMFtoJar** (version Replit) :

<img width="1105" height="713" alt="image" src="https://github.com/user-attachments/assets/97b48583-eb8c-425e-bbcc-a3b29523e51f" />




> *L’interface permet de choisir un fichier `.zip` contenant les sources du projet Java ME
> et de générer automatiquement un fichier `.jar` exécutable directement téléchargeable.*

```

---

💡 une **capture d’écran simulée** propre (interface claire avec boutons “Choose file” et “Compile JAR”) et le téléchargement:

```

<img width="1105" height="713" alt="image" src="https://github.com/user-attachments/assets/2cbf485c-a9fe-4098-931d-49ed3f40847e" />



