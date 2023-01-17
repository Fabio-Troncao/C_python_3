# if / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

# Ao observar as candicoes mesmo a condicao 4 tambem sendo True
# A condicao 3 aparece primeiro entao sempre vai 
# Ser realizado a condicao verdadeira que aparecer primeiro.

# posso ter if sozinho mas nao elif ou else.
#ja o else sempre vai ser a ultima condicao

if condicao1:
    print('Este e o codigo do primeiro if condicao 1')
elif condicao2:
    print('Codigo para condicao 2')
elif condicao3:
    print('Codigo para condicao 3')
elif condicao4:
    print('Codigo para condicao 4')
else:
    print('Este e o ELSE do primeiro if, onde nenhuma condicao foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('FORA DO IF...')