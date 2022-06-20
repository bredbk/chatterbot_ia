import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot('Robô atendente de refrigeração')

    

    def testar_microondas_parou(self):
        resposta = self.robo.get_response("meu microondas parou de funcionar")

        self.assertIn("Qual a marca e modelo do microondas que está com problema?", resposta.text)
    
    def testar_microondas_so_gira(self):
        resposta = self.robo.get_response("gira só o prato")

        self.assertIn("defeito no magnetron", resposta.text)

    def testar_nao_responde_painel(self):
        resposta = self.robo.get_response("painel não responde o comando")

        self.assertIn("Quase certeza que pode ser defeito na membrana", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)