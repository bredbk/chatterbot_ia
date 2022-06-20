from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

CONFIGURAÇÕES_CONVERSAS = [
    "C:/Users/bredbk/Desktop/chatterbot/chatterbot_ia/conversas_saudacoes.json",
    "C:/Users/bredbk/Desktop/chatterbot/chatterbot_ia/informações_basicas.json",
    "C:/Users/bredbk/Desktop/chatterbot/chatterbot_ia/conversas_geladeira.json",
    "C:/Users/bredbk/Desktop/chatterbot/chatterbot_ia/conversas_microondas.json",
    "C:/Users/bredbk/Desktop/chatterbot/chatterbot_ia/conversas_maquina.json"
]

def iniciar():
    global robo
    global treinador

    robo = ChatBot('Robô atendente de refrigeração')
        
    treinador = ListTrainer(robo)
    

def carregar_conversas():
    conversas = []

    for arquivo_configuracao in CONFIGURAÇÕES_CONVERSAS:
        with open(arquivo_configuracao, 'r') as arquivo:
            conversas_configuradas = json.load(arquivo)
            conversas.append(conversas_configuradas["conversas"])   # Adicionando as conversas configuradas
            arquivo.close()

    return conversas

def treinar_robo(conversas):
    global treinador

    for conversa in conversas:
        for mensagem_resposta in conversa:
            mensagens = mensagem_resposta["mensagens"]
            resposta = mensagem_resposta["resposta"]

            print("treinando o robô para responder a: ",mensagens, " com a resposta: ",resposta)
            for mensagem in mensagens:
                treinador.train([mensagem, resposta])
                

    


if __name__ == '__main__':
    iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar_robo(conversas)