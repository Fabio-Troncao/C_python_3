# if / elif      / else
# se / se não se / se não

entrada = input('Quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Entrou no sistema')
    #aqui so aparece o que estiver dentro dos blocos em que entra.
    print(2023)
elif entrada == 'sair':
    print('Saio do sistema')
else:
    print('Nao digitou nem entrar nem sair.')

print('FORA DOS BLOCOS')