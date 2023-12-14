# Calculateur de Panier

Le Calculateur de Panier est un outil en Python qui permet de calculer le prix total d'un panier d'achats en tenant compte de règles spécifiques, notamment des remises pour l'achat de plusieurs films de la saga "Retour vers le Futur".

## Table des matières

- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Démarrage](#démarrage)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
- [Utilisation](#utilisation)


## Introduction

Le Calculateur de Panier a été créé pour aider les utilisateurs à calculer le prix total de leur panier d'achats, en prenant en compte différentes règles de tarification pour les films, notamment ceux de la saga "Retour vers le Futur".

## Fonctionnalités 'énoncé'

Note avant de commencer : le livrable doit être fait comme s'il était réalisé pour un client et que vous initiiez ce programme pour travailler ensuite en équipe. Il doit être exemplaire.

L'équipe de production de Back to the Future voudrait remettre au goût du jour sa saga avec une technique marketing imparable :

revenir dans le passé, en 2000 ! Et passer un deal super smart avec une boutique de vente de DVDs (vous vous rappelez encore ce que c'est on espère...) avec une promo qui déchire :

le dvd d'un volet de la saga vaut 15€
pour l'achat 2 volets DIFFÉRENTS de la saga, on applique une réduction de 10% sur l'ensemble des DVDs "Back to the Future" achetés
pour l'achat de 3 volets DIFFÉRENTS de la saga, on applique une réduction de 20% sur l'ensemble des DVDs "Back to the Future" achetés
La boutique de DVDs vend également d'autres films qui coûtent chacun 20€.

Portant la lourde responsabilité de réparer les failles temporelle, l'équipe de production vous charge d'écrire un programme qui aura le comportement suivant :

En entrée, un panier sous forme de texte, séparé par des retours à la ligne qui contient le nom des films achetés
En sortie, le nombre représentant le prix
Vous êtes libre de montrer le résultat de la manière qui vous convient et cela peut rester très minimaliste, tant qu'il est clair que le programme sait lire le format d'entrée et qu'il suit bien les règles spécifiées. Néanmoins, comme indiqué en début d’énoncé, ce code devra être traité comme si vous l’initiiez pour votre future équipe.

Vous pourrez choisir le langage qui vous paraîtra le plus pertinent (dans lequel vous êtes à l'aise, c'est mieux), et qui devra pouvoir s'exécuter sur une JVM ou en Python. Vous vous assurerez que le livrable permette à quelqu'un ayant le SDK adéquat de lancer, utiliser et maintenir votre programme aisément. En résumé, le code doit être de très bonne qualité.

L’exercice est prévu pour ne pas vous demander plus de 30 minutes. Lors de l’éventuel entretien, venez avec votre code sur votre PC (pour vous permettre d’avoir un support sur lequel vous avez la main).

## Démarrage

### Prérequis

- Python 3.x

### Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Mohammedbasta/exercie_EKINOX.git

### Utilisation

- La classe PanierCalculator doit etre importée pour être utilisée
- La methode prix_panier accepte une liste des films ou le chemin vers un fichier txt
- Les tests ont été mise en place avant le developpement du calculateur en utilisant la librairie Unittest de Python
- Vous pouver executer le script de test test_TDD.py pour s'assurer du bon fonctionnement du calculateur
- les tests ont été faites pour analyser :
      * tester la précision des resultats globales de l'exercice 
      * tester la fonction qui calcule la precision
      * tester les resultats du calculator sur les exemples données dans l'énoncé
      * tester la performance du calculateur avec 3 millions de lignes
