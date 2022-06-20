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
        resposta = self.robo.get_response("em que horário você atende?")

        self.assertIn("Atendo das 10h da manhã ás 18h da tarde", resposta.text)
    
    def testar_autorizada(self):
        resposta = self.robo.get_response("você é da autorizada?")

        self.assertIn("Não somos autorizada", resposta.text)

    def testar_garantia(self):
        resposta = self.robo.get_response("quanto tempo tem a garantia?")

        self.assertIn("A garantia do serviço realizado é de 90 dias", resposta.text)

    def testar_marca(self):
        resposta = self.robo.get_response("electrolux")

        self.assertIn("Descreva em poucas palavras", resposta.text)

    def testar_atendimento(self):
        resposta = self.robo.get_response("você atende a domicilio?")

        self.assertIn("Atendemos a domicilio", resposta.text)

    

if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacoes))

    executor = unittest.TextTestRunner()
    executor.run(testes)