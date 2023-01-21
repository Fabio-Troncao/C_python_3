# Operadores in e not in
# Strings são iteráveis ou seja se pode navegar item por item
#  0 1 2 3 4
#  F á b i o
# -5-4-3-2-1
# nome = 'Fábio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('á' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')