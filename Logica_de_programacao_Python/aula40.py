"""Calculadora com while, de forma mais completa com validação"""

while True:
    numero_1 = input ('Digite um número: ')
    numero_2 = input ('Digite outro número: ')
    operador = input ('Digite o operador (+-/*): ')
    # Iniciando validações de possives erros realizados pelo usuario.
    numeros_validos = None # Aqui irei criar uma flag.
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True # Aqui caso a converção do numero 1 e 2 seja ok entao a flag passa a True.
    except: #Obs: aqui poderiamos usar o except Exception para printar o possivel erro. Mas por agora nao usaremos.
        numeros_validos = None #Aqui usaremos para confirmação do dado ser um numero ou nao, em um booleano.

    if numeros_validos is None: # Aqui caso a flag seja True ele nao executa a condição, mas caso seja None, ele entra informa a mensagem.
        print('Um ou ambos os números digitados são invãlidos. ')
        continue # E chegando ao continue ele entao inicia novamente o laço do while.
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos: #Aqui irei confirmar se o operador inserido pelo usuario está entre os operadors permitidos que deixei na variavel.
        print('Operador invãlido. ')
        continue #Aqui como ja foi falado. Chegando aqui ele inicia o laço while.

    if len(operador) > 1:# Aqui so irei confirmar se o usuario usou apenas um operador ou mais. caso mais que 1 aparece a mensageme e inicia o laço tambem.
        print('Digite apenas um operador. ')
        continue

    # Finalizando validações de possives erros realizados pelo usuario.
    # Iniciando o calculo do exercicio.

    print('Realizando sua conta. Confira o resultado abaixo: ')
    if operador == '+':
        print(f'{numero_1_float}+{numero_2_float}=', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float}-{numero_2_float}=', numero_1_float - numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float}/{numero_2_float}=', numero_1_float / numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float}*{numero_2_float}=', numero_1_float * numero_2_float)
    else:
        print("Nunca deveria chegar aqui!!! ") #Se por acaso chegar aqui. visualizar o erro e incrementar na validação de possiveis erros.

    #############
    #sair = input("Quer sair? [s]im: ")
    #sair = sair.lower() # lower para deixar string com as letras minúsculas. Obs: todos esses comandos se encontram na decomentação do Python.
    #sair = sair.startswith('s') #Neste caso utilizar startswith para saber a primeira letra da string. Obs: endswith seria para saber a ultima letra da string.
    # Obs: O mesmo codigo em cima que está em 3 linhas (para uma melhor compreensão) pode ser feito em uma como realizado abaixo. 
    sair = input("Quer sair? [s]im: ").lower().startswith('s')

    if sair is True:
        break