#nome = input('Qual o seu nome? ')
#print(f'O seu nome e {nome}')

# Dessa forma tanto o numero_1 como numero_2 sao STR
# Por isso em vez de somar ele vai concatenar.
numero_1 = input('Digite um numero. ')
numero_2 = input('Digite outro numero. ')

print(f'O seu nome e {type(numero_1 + numero_2)}')
print(f'O seu nome e {numero_1 + numero_2}')

numero_3 = input('Digite um numero. ')
numero_4 = input('Digite outro numero. ')

#Neste caso aqui o tipo vai ser int pois esta sende passado para formato inteiro.
int_numero_3 = int(numero_3)
int_numero_4 = int(numero_4)

print(f'O seu nome e {type(int_numero_3 + int_numero_4)}')
print(f'O seu nome e {int_numero_3 + int_numero_4}')