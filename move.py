import pyttsx3


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
        operacao = str(input("Operações: (1-Consultar, 2-Transferir, 3- Ver Extrato)        "))

        if operacao.lower() in('consultar', '1', 1):
            speak("Ok, estou trabalhando nisso!")

        elif operacao.lower() in('transferir','2',2):
            speak("Ok, estou trabalhando nisso!")
            
        elif operacao.lower() in('ver extrato','3',3):
            speak("Ok, estou trabalhando nisso!")

        else:
            speak("Operação inexistente")
            num=0

    else:
        speak("Ok, encerrando a sessão, até mais")
        num=0