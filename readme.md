![Logo](litreview/static/img/LITReview_logo.png)

# Projet 9 DA-Python OC
***Livrable : MVP de LITReview, site communautaire de critiques de livres..***

Testé sous Windows 11 - Python version 3.10.5 - Django 4.1.2


## Sommaire

**[1. Installation et lancement du projet](#heading--1)**
  * [1.1. Windows](#heading--1-1)
  * [1.2. MacOS et Linux](#heading--1-2)

**[2. Fonctionnalités et ultilisation](#heading--2)**
  * [2.1 Fonctionnalités](#heading--2-1)
  * [2.2 Utilisation](#heading--2-2)

       

<div id="heading--1"/>

### 1. Installation et lancement du projet

<div id="heading--1-1"/>

#### 1.1 Windows :
   Depuis votre terminal, naviguez vers le dossier racine souhaité.

###### Récupération du projet
   Tapez :    

       git clone https://github.com/Cyl94700/P9_Op_Cl.git

###### Accéder au dossier du projet, créer et activer l'environnement virtuel
   Tapez :

       cd P9_Op_Cl
       python -m venv env 
       env\scripts\activate
    
###### Installer les paquets requis
   Tapez :

       pip install -r requirements.txt
       cd litreview 

###### Lancer le serveur Django
   Tapez :

      python manage.py runserver

###### Vous pouvez ensuite utiliser le site à l'adresse suivante :
   Depuis votre navigateur, tapez :

      http://127.0.0.1:8000


<div id="heading--1-2"/>

---------

####  1.2 MacOS et Linux :
   Depuis votre terminal, naviguez vers le dossier souhaité.

###### Récupération du projet
   Tapez :

       git clone https://github.com/Cyl94700/P9_Op_Cl.git

###### Activer l'environnement virtuel
   Tapez :

       cd P9_Op_Cl
       python -m venv env 
       source env/bin/activate
    
###### Installer les paquets requis
   Tapez :

       pip install -r requirements.txt
       cd litreview

###### Lancer le serveur Django
   Tapez :

       python manage.py runserver

###### Vous pouvez ensuite utiliser le site à l'adresse suivante :
   Depuis votre navigateur, tapez :

      http://127.0.0.1:8000


<div id="heading--2"/>

### 2. Fonctionnalités et utilisation

<div id="heading--2-1"/>

#### 2.1 Fonctionnalités

- Se connecter et s'inscrire.
- Consulter son profil et le modifier (nom d'utilisateur et photo de profil).
- Consulter un fil classé par orde chronologique contenant tickets et critiques des utilisateurs auxquels on est abonné. 
- Créer des tickets (demande de critique sur un livre/article).
- Créer des critiques, en réponse ou non à des tickets. 
- Filtre sur tickets ou critiques avec possibilité de les modifier ou les supprimer. 
- Suivre d'autres utilisateurs, ou se désabonner.
- Voir qui l'on suit et par qui l'on est suivi.


<div id="heading--2-2"/>

#### 2.2 Utilisation

#### Django administration

Identifiant : **admin** | Mot de passe : **admpwd123**

&rarr; http://127.0.0.1:8000/admin/

#### Liste des utilisateurs existants

| *Identifiant* | *Mot de passe* |
|---------------|----------------|
| admin         | admpwd123      |
| Bibliophile04 | password999    |
| Emilie75      | password999    |
| Jean23        | password999    |
| Ulysse55      | password999    |


