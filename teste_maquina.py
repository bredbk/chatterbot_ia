import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot('Robô atendente de refrigeração')

    

    def testar_maquina_parou(self):
        resposta = self.robo.get_response("minha maquina parou de funcionar")

        self.assertIn("Qual a marca e modelo da máquina de lavar", resposta.text)
    
    def testar_so_gira(self):
        resposta = self.robo.get_response("não gira o cesto")

        self.assertIn("pode ser defeito no atuador", resposta.text)

    def testar_nao_joga_agua(self):
        resposta = self.robo.get_response("não joga água fora")

        self.assertIn("pode ser defeito na bomba de drenagem", resposta.text)

    def testar_nao_enta_agua(self):
        resposta = self.robo.get_response("não entra água")

        self.assertIn("certeza que pode ser defeito na válvula de entrada", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)