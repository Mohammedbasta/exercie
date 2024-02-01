import os, logging, sys
from pathlib import Path, PureWindowsPath


class PriceCalculationError(Exception):
    pass


class PanierCalculator:
    def __init__(self):
        # Configure the logging module
        logging.basicConfig(level=logging.INFO)


    def read_file(self, file_path):
        """
       Lit les films depuis un fichier et retourne une liste de films.

       Paramètres :
       - file_path (str) : Le chemin du fichier.

       Retourne :
       - List[str] : Liste des films lues depuis le fichier.
       """
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except:
            filename = PureWindowsPath(file_path)
            correct_path = Path(filename)
            with open(correct_path, 'r') as file:
                return [line.strip() for line in file.readlines()]


    def prix_panier(self, input_data):
        """
        Calcule le prix d'un panier des films.

        Paramètres :
        - input_data (str ou list) : Les données d'entrée, soit un chemin de fichier soit une liste de films.

        Retourne :
        - float : Le prix calculé.
        """


        try:
            # pour gérer la lecture des données
            if input_data is None or (isinstance(input_data, str) and not input_data.strip()):      # Validation de l'entrée
                raise ValueError("L'entrée ne peut pas être vide.")

            if isinstance(input_data, str):
                # Si input_data est une string, c'est un chemin de fichier
                panier = self.read_file(input_data)
            elif isinstance(input_data, list):
                # Si input_data est une liste, c'est une liste de lignes
                panier = input_data
            else:
                raise ValueError("L'entrée doit être soit un chemin de fichier (chaîne de caractères) soit une liste de lignes.")

            # le contenu de la fonction commence ici
            dvd = 15            # Le prix d'un dvd Back to the Future
            other_films = 20    # Le prix des autres film

            # pour gérer la fréquence des films de la saga
            bttf_films = [film for film in panier if "Back to the Future" in film]
            unique_bttf_films = set(bttf_films)
            other_movies = [film for film in panier if "Back to the Future" not in film]

            # Calculer le prix en fonction du nombre de films différents de la saga
            if len(unique_bttf_films) >= 3:                                             # Réduction de 20% pour l'achat de 3 films ou plus différents de la saga
                return len(bttf_films) * dvd * 0.8 + len(other_movies) * other_films
            elif len(unique_bttf_films) >= 2:                                           # Réduction de 10% pour l'achat de 2 films différents de la saga
                return len(bttf_films) * dvd * 0.9 + len(other_movies) * other_films
            else:                                                                       # Aucune réduction pour un seul film de la saga
                return len(bttf_films) * dvd + len(other_movies) * other_films
        except PriceCalculationError as e:
            # Log the error
            logging.error(f"An error occurred: {e}")
            # Raise a custom exception ou returner une erreur code 
            raise f"An error occurred during price calculation. {e}"
