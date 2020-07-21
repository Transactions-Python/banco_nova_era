import os

def cadastrarAdministrador():
    n = input('Digite o nome: ')
    s = input('Digite o sobrenome: ')
    t = int(input('Digite o telefone: '))
    e = input('Digite o email: ')
    agenda = open('%s_%s.txt' %(n,s),'a')
    agenda.write('%s %s, %d, %s\n'%(n, s, t, e))
    agenda.close()

def buscarAdministrador():
    n = input('Digite o nome do administrador a ser pesquisado: ')
    s = input('Digite o sobrenome do administrador a ser pesquisado: ')

    if os.path.isfile('%s_%s.txt'%(n,s)):
          agenda = open('%s_%s.txt'%(n,s),'r')
    
          for x in agenda.readlines():
                print(x)
          agenda.close()

    else:
       print('Administrador não encontrado.') 


    

def deletarAdministrador():
    n = input('Digite o nome que deseja apagar: ')
    s = input('Digite o sobrenome que deseja apagar: ')
    os.remove('%s_%s.txt'%(n,s))



def main():
    print('              MENU')
    print('1. Novo Administrador\n2. Buscar administrador pelo nome')
    print('3. Atualizar administrador\n4. Apagar administrador\n0. Sair')
    op = 1
    while op!=0:
        op = int(input('\nDigite a opção: '))
        if op==1:            
            cadastrarAdministrador()            
        elif op==2:
            buscarAdministrador()
        elif op==4:
            deletarAdministrador()     
        elif op==0:
            print('Saindo....')
            break
        else:
            print('Opção incorreta, tente novamente. ')
main()