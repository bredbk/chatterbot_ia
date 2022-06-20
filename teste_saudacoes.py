import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot('Robô atendente de refrigeração')

    def testar_oi(self):
        resposta = self.robo.get_response("oi")
        self.assertIn("Saudações, sou o robô assistente", resposta.text)

    def testar_bom_dia(self):
        resposta = self.robo.get_response("bom dia")

        self.assertIn("Bom dia sou o robô assistente", resposta.text)
    
    def testar_boa_noite(self):
        resposta = self.robo.get_response("boa noite tudo bem?")

        self.assertIn("Boa noite sou o robô assistente", resposta.text)

    def testar_horario(self):
        resposta = self.robo.get_response("atende em qual horario? é da autorizada?")

        self.assertIn("Atendo das 10h da manhã ás 18h da tarde", resposta.text)
    
    def testar_horario(self):
        resposta = self.robo.get_response("é da autorizada?")

        self.assertIn("Não somos autorizada", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)