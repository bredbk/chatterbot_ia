from chatterbot import ChatBot

def executar_robo():
    robo = ChatBot('Robô atendente de refrigeração')

    while True:
        pergunta = input('Digite algo ...: ')
        resposta = robo.get_response(pergunta)
        if resposta.confidence > 0.5:
            print('Robô: ', resposta.text)
        else:
            print('Robô: Ainda não sei responder a isso!')
    

if __name__ == '__main__':
    executar_robo()