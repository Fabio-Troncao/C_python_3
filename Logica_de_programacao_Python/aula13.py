nome = 'Fabio Troncao'
altura = 1.92
peso = 101
imc = ... # IMC = peso / (altura x altura)

imc = peso / (altura * altura)

# f-strings quer dizer formatacao
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC e imc'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

print('Fabio Troncao tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu IMC e', imc)

print(...)

# Fabio Troncao tem 1.92 de altura
# pesa 101 quilos e seu IMC e
# 