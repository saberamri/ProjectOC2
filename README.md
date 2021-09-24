## Table des matière
1. [Description_projet](#Description_projet)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Statut_projet](#Statut_projet)

### Description générale du projet
***
Objet : Programme d'extraction des prix: Créer un système de surveillance des prix. 

- Choisir n'importe quelle page Produit sur le site de Books to Scrape. Écrire un script Python qui visite cette page et en extrait les informations suivantes:

product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url

- Écrire les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.
- Récupérer toutes les données nécessaires pour toute une catégorie d'ouvrages. Choisir n'importe quelle catégorie sur le site de Books to Scrape. Écrire un script Python 
qui consulte la page de la catégorie choisie, et extrait l'URL de la page Produit de chaque livre appartenant à cette catégorie. 
- Combiner cela avec le travail effectué afin d'extraire les données produit de tous les livres de la catégorie choisie. 
- écrivez les données dans un seul fichier CSV.
- écriture d'un script qui consulte le site de Books to Scrape, extrait toutes les catégories de livres disponibles, puis extrait les informations 
produit de tous les livres appartenant à toutes les différentes catégories.
- écrire les données dans un fichier CSV distinct pour chaque catégorie de livres. 

## Technologies
***
A list of technologies used within the project:
* [Python](https://www.anaconda.com/products/individual-d): Version Python 3.8.5

## Installation
***
Pour installer des bibliothèques Python bien spécifiques, nous avons développé un environnement virtuel "venv" dans le répertoire développement.
```
1. Accédez au répertoire dans lequel vous créez un environnement virtuel:
$ cd /repertoire développement
$ python -m  venv venv

2.Activer l’environnement avec:
$ .\venv\Scripts\Activate.ps1

3.Installer les dépendances requises avec pip install -r requirements.txt

4.Exécuter à partir de la ligne de commande ou du terminal python le programme principal avec la commande:
$ python main.py

5.Pour terminer,  désactiver l’environnement virtuel avec 
$ .deactivate

```
## Statut du projet: 
Le développement du projet est en cours.
