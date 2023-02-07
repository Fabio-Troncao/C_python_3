"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

"""numero_int = input('Digite um numero inteiro: ')

try:
    numero_int = int(numero_int)
    if numero_int %2 == 0:
        print('Seu numero é par.')
    else:
        print('Seu numero é ímpar')
except:
    print('O que digitou não é um número inteiro')"""

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

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) >=5 and len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")