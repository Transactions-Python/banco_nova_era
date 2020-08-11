import os
import time
from cadastro import main as cd
def principal():
    lista = [] 
    while True:
        time.sleep(2)
        os.system("cls");
        print(" MÓDULO ADM")
        print("1 - Acessar área de alimentação de cédulas")
        print("2 - Sangria")
        print("3 - Acessar área de relatórios")
        print("4 - Cadastrar Administrador")
        print("5 - Sair")
       
        opcao = int(input("Digite qual área gostaria de acessar:"))

        if opcao == 1:
            print("\n  Trata-se basicamente da reposição de notas no caixa. Nesta area vai ser definida qual é o valor em que o caixa entra em sinal vermelho e necessita da realimentação de cédulas, para que assim seja enviado mais cédulas aquele caixa eletrônico. ")
        # Aqui area de alimentação de cédulas
            time.sleep(9)

        if opcao == 2:
            print("\n Quando o dinheiro for deslocado do local sem ser de forma planejada do banco, ele será levado para outro lugar mais especifico (por questões de segurança):")
            time.sleep(9)
        # Aqui a área da sangria

        if opcao == 3:
        
            print("\n nesta área caixa emitira um relatório para que nós do administrativo tenhamos controle de suas movimentações em determinado período de tempo, como por exemplo a quantidade de extratos emitidos, saques, depósitos, transferências e toda a quantia de dinheiro envolvida nestes processos.")
            time.sleep(9)
    
            #Aqui a area de relatórios onde irá gerar um arquivo txt

        if opcao == 4:
            cd()
            # Aqui a area para cadastro
      

        if opcao == 5:
            print("\n Saindo do Programa...")
            break 

        

principal()
