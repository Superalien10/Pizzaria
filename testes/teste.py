import sys


import pizzza
import unittest
from datetime import date
from unittest.mock import Mock

def setUpModule():
    print('\nExecutando SetUpModule')

def tearDownModule():
    print('\nExecutando tearDownModule')

class TestModuloQualidade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\nExecutando setUpClass')
    @classmethod
    def tearDownClass(cls):
        print('\nexecutando tearDownClass')
    def setUp(self):
        print('\nExecutando setUpClass')
    def tearDown(self):
        print('\nExecutando tearDownMethod')
    def test_case_pizza_calabresa(self):
        print('Teste de montar pizza de calabresa')
    def test_case_comum(self):
        print("Executando Caso de Teste: Comum")
        self.assertEqual( pizzza.remover_ingrediente("cobertura", "pepperoni"), {'massa': {'trigo': 19.34}, 'molho': {'tomate': 5}, 'cobertura': {}, 'queijo': {'gorgonzola': 2}})
        
if __name__ == '__main__':
    unittest.main(verbosity=2)