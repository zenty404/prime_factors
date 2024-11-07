# Facteurisation en Nombres Premiers - Projet NSI Terminale

Ce projet est une application développée en Python avec une interface graphique (Tkinter) permettant de factoriser un nombre entier en ses facteurs premiers. Il s’inscrit dans le cadre de la spécialité NSI (Numérique et Sciences Informatiques) en terminale.

## Objectifs du Projet

L’objectif principal est de **tester les performances d’un algorithme récursif** de factorisation en nombres premiers, avec la possibilité de configurer la profondeur de recherche. L’interface permet d’entrer un nombre entier, de définir une limite pour les diviseurs, et d’afficher le temps d’exécution de l’algorithme.

## Fonctionnalités

1. **Saisie d'un nombre entier** : L’utilisateur peut entrer un nombre à factoriser en nombres premiers.
2. **Limite de diviseur** : L’utilisateur peut configurer une limite maximale pour le diviseur, influençant la profondeur de recherche et les performances.
3. **Affichage du temps d'exécution** : Une option permet d’afficher le temps d’exécution de l’algorithme.
4. **Résultats clairs** : Les facteurs premiers et le temps d’exécution (si activé) s’affichent dans l’interface.
5. **Interface intuitive** : Accessible à des utilisateurs non spécialistes.

## Pré-requis

- **Python 3.x** : Ce programme nécessite une version récente de Python.
- **Tkinter** : Bibliothèque intégrée dans Python pour les interfaces graphiques.

## Installation et Lancement

1. Clonez le dépôt GitHub pour obtenir le code source :

    ```bash
    git clone https://github.com/zenty404/prime_factors.git
    cd prime_factors
    ```

2. Assurez-vous que vous avez Python et Tkinter installés :

    ```bash
    python --version
    ```

3. Lancez le programme en exécutant le fichier principal :

    ```bash
    python main.py
    ```

## Utilisation

1. **Entrez un nombre** dans le champ prévu.
2. **Définissez la limite de diviseur** en ajustant le curseur.
3. **Activez ou désactivez** l’option pour afficher le temps d’exécution.
4. Cliquez sur **"Lancer la factorisation"** pour voir les résultats.
5. Cliquez sur **"Réinitialiser"** pour remettre à zéro les champs et paramètres.

## Structure du Code

Le code est structuré de la manière suivante :

- **Fonction récursive de factorisation** : Utilise la récursivité pour décomposer le nombre en facteurs premiers.
- **Interface Tkinter** : Comprend différents widgets (Label, Entry, Scale, Checkbutton, et Button) pour interagir avec l’utilisateur et afficher les résultats.
- **Gestion des erreurs** : Envoie un message d'erreur si l’utilisateur entre une valeur invalide.

## Exemples d'Utilisation

- **Nombre à factoriser** : 105
- **Limite de diviseur** : 50
- **Résultats attendus** : `Facteurs premiers : [3, 5, 7]`

## Analyse des Performances

L’algorithme est optimisé pour fonctionner rapidement sur des nombres de taille modeste. En limitant la valeur des diviseurs, il est possible d’analyser l'impact de la profondeur de recherche sur le temps d'exécution.

## Contributions

Les contributions sont les bienvenues pour améliorer ce projet ! Si vous avez des suggestions ou des corrections, veuillez ouvrir une issue ou un pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus d’informations.
