import unittest
from robo import *

class TesteMicroondas(unittest.TestCase):

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

    def testar_placa(self):
        resposta = self.robo.get_response("o visor não acende")

        self.assertIn("Quase certeza que pode ser defeito na placa", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteMicroondas))

    executor = unittest.TextTestRunner()
    executor.run(testes)