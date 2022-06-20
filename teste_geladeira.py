import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot('Robô atendente de refrigeração')

    

    def testar_geladeira(self):
        resposta = self.robo.get_response("geladeira não gela")

        self.assertIn("Qual a marca da geladeira", resposta.text)
    
    def testar_nao_funciona(self):
        resposta = self.robo.get_response("geladeira não está funcionando")

        self.assertIn("Qual a marca da geladeira que está com problema?", resposta.text)

    def testar_congelador(self):
        resposta = self.robo.get_response("congelador gela muito")

        self.assertIn("sensor ou resistência ou capa traseira", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)