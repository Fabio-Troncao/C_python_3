# if / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = True

#Na realizacao do DEBUG add o brackpoint e passamos linha a linha para visualizar melhor.
#E em relacao a este codigo se pormos um brackpoint na linha 4
# e passarmos linha a linha podemos visualisar que ele so vai entrar no bloco da Condicao 3

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