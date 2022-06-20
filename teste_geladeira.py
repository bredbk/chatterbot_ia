import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot('Robô atendente de refrigeração')

    

    def testar_geladeira_parou(self):
        resposta = self.robo.get_response("minha geladeira deu defeito")

        self.assertIn("Qual a marca da geladeira que está com problema?", resposta.text)
    
    def testar_nao_funciona(self):
        resposta = self.robo.get_response("minha geladeira não está funcionando")

        self.assertIn("Qual a marca da geladeira que está com problema?", resposta.text)

    def testar_congelador(self):
        resposta = self.robo.get_response("congelador gela muito")

        self.assertIn("sensor ou resistência ou capa traseira", resposta.text)
    
    def testar_parou_de_gelar(self):
        resposta = self.robo.get_response("parou de gelar as duas partes")

        self.assertIn("O problema pode ser o gás mas tem que testar", resposta.text)

    def testar_parou_de_gelar(self):
        resposta = self.robo.get_response("está perdendo tudo na geladeira")

        self.assertIn("Paciencia, vamos resolver, poderia informar a marca e o modelo", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)