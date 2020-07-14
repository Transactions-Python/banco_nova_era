print("1 - ADMINISTRATIVO\n2 - CLIENTE\n3 - MOVIMENTAÇÃO")

select = str(input("Digite aqui qual módulo irá acessar...      "))

if select.lower() in('1', 'administrativo'):
    from admin import *

elif select.lower() in('2', 'cliente'):
    from client import *

elif select.lower() in('3', 'movimentação', 'movimentacao'):
    from move import *

else:
    print("Esse módulo não existe")