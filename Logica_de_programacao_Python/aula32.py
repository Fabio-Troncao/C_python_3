"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')"""


"""numero = input('Digite um número: ')

try:
    numero_int = float(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {numero_int} é {par_impar_texto}')
except:
    print('Você não digitou um número')"""


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""hora = input('Digite a hora em número inteiro: ')

try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <=11:
        print('Bom dia')
    elif hora_int >= 12 and hora_int <=17:
        print('Boa tarde')
    elif hora_int >= 18 and hora_int <=23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apena numero inteiro')"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite pelo menos uma letra.')

#######################################################################################
"""numero_int = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero_int)
    if numero_int %2 == 0:
        print('Seu numero é par.')
    else:
        print('Seu numero é ímpar')
except:
    print('O que digitou não é um número inteiro')"""

######################################################

"""hora = input('Digite a hora: ')
hora = int(hora)
bom_dia = hora >= 0 and hora <= 11
boa_tarde = hora >= 12 and hora <= 17
boa_noite = hora >= 18 and hora <= 23

if bom_dia:
    print('Bom Dia!!!')
elif boa_tarde:
    print('Boa Tarde!!!')
elif boa_noite:
    print('Boa noite!!!')
else:
    print('Informação digitada incorreta!!!')"""

###########################################################

"""nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >=5 and len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")"""