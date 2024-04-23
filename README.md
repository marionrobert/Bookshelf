# Application de Gestion de Collection de Livres

## Introduction
Ce projet consiste à créer une application web permettant aux utilisateurs de gérer une collection de livres en ajoutant, modifiant et supprimant des livres dans une base de données SQLite à l'aide de Flask et SQLAlchemy.

## Fonctionnalités
- Affichage de la liste des livres existants.
- Ajout d'un nouveau livre avec titre, auteur et évaluation.
- Modification de l'évaluation d'un livre existant.
- Suppression d'un livre de la collection.

## Exigences
- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation et Configuration
1. Assurez-vous d'avoir Python installé sur votre système.
2. Installez les packages requis en utilisant pip et le fichier `requirements.txt`: `pip install -r requirements.txt`.
3. Assurez-vous d'avoir un navigateur Chrome installé sur votre système (pour le développement et les tests).
4. Exécutez le script `main.py` pour démarrer l'application Flask.

## Utilisation
1. Accédez à l'URL fournie par Flask dans votre navigateur.
2. Sur la page d'accueil, vous pouvez voir la liste des livres existants et ajouter de nouveaux livres.
3. Vous pouvez également modifier ou supprimer des livres en utilisant les liens correspondants.

## Structure du Projet
- `main.py`: Le script principal de l'application Flask.
- `templates/`: Répertoire contenant les fichiers HTML pour les pages web.
    - `index.html`: Page d'accueil affichant la liste des livres et les options pour ajouter, modifier et supprimer des livres.
    - `add.html`: Formulaire pour ajouter un nouveau livre à la collection.
    - `edit.html`: Formulaire pour modifier l'évaluation d'un livre existant dans la collection.
- `static/`: Répertoire optionnel pour les fichiers statiques comme les feuilles de style CSS ou les scripts JavaScript (non utilisé dans cet exemple).
- `new-books-collection.db`: Fichier de base de données SQLite pour stocker les informations sur les livres.
- `requirements.txt`: Fichier contenant la liste des packages Python nécessaires pour l'application.

## Remarques
- Ce projet utilise Flask comme framework web pour Python.
- SQLAlchemy est utilisé pour la gestion de la base de données SQLite et la manipulation des objets Python.
- Assurez-vous de configurer les variables d'environnement et les chemins appropriés selon votre configuration système.
- Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) d'Angela Yu sur la plateforme Udemy.

Vous pouvez ajouter des instructions supplémentaires sur la configuration de l'environnement, l'utilisation des fonctionnalités, et d'autres détails spécifiques selon vos besoins. N'hésitez pas à personnaliser le contenu du README en fonction des détails uniques de votre projet.
