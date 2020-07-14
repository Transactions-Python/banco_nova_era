<<<<<<< HEAD:client.py
import os


def Cadastrar():
    nome_empre = input('Digite o Nome da Empresa: ')
    cnpj = int(input('Digite o CNPJ da Empresa: '))
    local = input('Digite Localização da Empresa: ')
    inscri = int(input('Digite a inscriçã estadual da Empresa: '))
    funcionalidades = input ('Digite as funcionalidades que deseja: ')
    arquivo = open ('%s_%d.txt' %(nome_empre,cnpj),'a')
    arquivo = open('%s_%d.txt' %(nome_empre,cnpj),'a')
    arquivo.write('%s_ %d, %s, %d, %s\n'%(nome_empre, cnpj, local, inscri, funcionalidades))
    arquivo.close()

def Cliente():
    print(' === MÓDULO CLIENTE === ')
    print('1 - Cadastrar Banco ou Fintech')
    print('2 - Editar Cadastro')
    print('3 - Listar Banco ou Fintech')
    print('4 - Sair do Sistema do Banco')
    opcao = int(input('\nDigite a opção: '))
    while opcao!=4: 
        if opcao == 1:
            Cadastrar()
        elif opcao == 2:
            Editar()
        elif opcao == 3:
            Listar()
        elif opcao == 4:
            print('\n Saindo do Programa...')
            break
        else:
            print ('opção incorreta tente novamente ')
Cliente()

=======
import os


def Cadastrar():
    nome_empre = input('Digite o Nome da Empresa: ')
    cnpj = int(input('Digite o CNPJ da Empresa: '))
    local = input('Digite Localização da Empresa: ')
    inscri = int(input('Digite a inscriçã estadual da Empresa: '))
    funcionalidades = input ('Digite as funcionalidades que deseja: ')
    arquivo = open ('%s_%d.txt' %(nome_empre,cnpj),'a')
    arquivo = open('%s_%d.txt' %(nome_empre,cnpj),'a')
    arquivo.write('%s_ %d, %s, %d, %s\n'%(nome_empre, cnpj, local, inscri, funcionalidades))
    arquivo.close()

def Cliente():
    print(' === MÓDULO CLIENTE === ')
    print('1 - Cadastrar Banco ou Fintech')
    print('2 - Editar Cadastro')
    print('3 - Listar Banco ou Fintech')
    print('4 - Sair do Sistema do Banco')
    opcao = 1
    while opcao!=4:
        opcao = int(input('\nDigite a opção: '))
        if opcao == 1:
            Cadastrar()
        elif opcao == 2:
            Editar()
        elif opcao == 3:
            Listar()
        elif opcao == 4:
            print('\n Saindo do Programa...')
            break
        else:
            print ('opção incorreta tente novamente ')
Cliente()

>>>>>>> 9b667eafc3cd328c71e16df721f0064fc5aad8b9:menu (2).py
