import pyttsx3
from connection import *


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait();

num = 1
speak("Olá, sou seu assistente, me chamo Renatinho, seja bem-vindo ao Banco Nova Era!")
while num==1:

    speak("Confirme se deseja prosseguir")
    choice = str(input("Deseja prosseguir?(S,Y,s,y)(N, N, n, n)         "))

    if choice.lower() in('s', 'y', 'sim'):
        speak("Qual operação deseja realizar?")
        operacao = str(input("Operações: (1- Consultar, 2- Criar conta, 3- Transferir, 4- Ver Extrato)        "))

        if operacao.lower() in('consultar', '1', 1):
            speak("Ok, estou trabalhando nisso!")
            
        elif operacao.lower() in('criar conta', '2', 2):
            speak("Ok, estou trabalhando nisso!")

        elif operacao.lower() in('transferir','3',3):
            speak("Ok, estou trabalhando nisso!")
            
        elif operacao.lower() in('ver extrato','4',4):
            speak("Ok, estou trabalhando nisso!")

        else:
            speak("Operação inexistente")
            num=0

    else:
        speak("Ok, encerrando a sessão, até mais")
        num=0
