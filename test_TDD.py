import unittest, logging, os, timeit
from PanierProcessor import PanierCalculator

calculator = PanierCalculator()
files_path = os.getcwd() + '\\examples\\'


class TestAccuracy(unittest.TestCase):                              # tester la fonction qui calcule la precision
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Initializing TestAccuracy ...")

    def test_accuracy(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'a': 1, 'b': 20, 'd': 4}
        self.assertEqual(accuracy_fortest(dict1, dict2), {'a': True, 'b': False})


class TestThePanierFctExamples(unittest.TestCase):                  # tester la précision des resultats globales de l'exercice
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Initializing TestThePanierFctExamples ...")

    def test_Panier_examples(self):
        examples = {
            'ex1': 36,
            'ex2': 27,
            'ex3': 15,
            'ex4': 48,
            'ex5': 56
        }

        survey_rslt = main_fct_fortest(examples)

        self.assertEqual(survey_rslt['ex1'], calculator.prix_panier(os.path.join(files_path, 'ex1')))
        self.assertEqual({'ex2': True, 'ex5': True, 'ex3': True, 'ex4': True, 'ex1': True}, accuracy_fortest(survey_rslt, examples))


class TestPrixPanier(unittest.TestCase):                            # tester les resultats du calculator avec les exemples dans l'email
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Initializing TestPrixPanier ...")

    def test_prix_panier(self):
        # test cases pour la fonction prix_panier
        self.assertEqual(calculator.prix_panier(os.path.join(files_path, 'ex1')), 36)
        self.assertEqual(calculator.prix_panier(os.path.join(files_path, 'ex2')), 27)
        self.assertEqual(calculator.prix_panier(os.path.join(files_path, 'ex3')), 15)
        self.assertEqual(calculator.prix_panier(os.path.join(files_path, 'ex4')), 48)
        self.assertEqual(calculator.prix_panier(os.path.join(files_path, 'ex5')), 56)


class TestPanierPerformance(unittest.TestCase):                     #tester la performance du calculateur avec 3 millions de lignes
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        logging.info("Initializing TestPanierPerformance ...")

    def test_performance(self):
        # Performance test with a large panier
        large_panier = ['Back to the Future {}'.format(i) for i in range(1, 30000000)]
        execution_time = timeit.timeit(lambda: calculator.prix_panier(large_panier), number=1)


# les fonctions pour aider au mieux tester


def accuracy_fortest(dict1, dict2):
    """
       fonction qui calcule la précision des calculs

       Paramètres :
       - Deux dictionnaires.

       Retourne :
       - dictionnaire : values True/False pour comparer les dicts.
    """

    common_keys = set(dict1) & set(dict2)
    return {key: dict1[key] == dict2[key] for key in common_keys}



def main_fct_fortest(example_dict):
    """
       fonction qui fait appel au calculator pour calculer les paniers des exemples dans le fichier ci-joint 

       Paramètres :
       - dict des example pour tester le calculateur.

       Retourne :
       - dict : values calculées avec lecalculateur du panier.
    """
    survey = {}
    for key, value in example_dict.items():
        file_path = os.path.join(files_path, key)
        try:
            survey[key] = calculator.prix_panier(file_path)
        except Exception as e:
            survey[key] = f'Exception: {e}'
    return survey



if __name__ == '__main__':
    print(calculator.prix_panier(files_path+'ex4'))
    unittest.main()



