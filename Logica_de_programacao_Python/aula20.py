#Exer. dada as proximas 2 linhas mostrar qual maior valor.
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor>segundo_valor:
    print(
        f'Primeiro valor = {primeiro_valor} é maior do que ' 
        f'segundo valor = {segundo_valor}. ')
elif primeiro_valor == segundo_valor:
    print(
        f'Primeiro valor = {primeiro_valor} é igual ao '
        f'segundo valor = {segundo_valor}. ')
else:
    print(
        f'Primeiro valor = {primeiro_valor} é menor do que '
        f'segundo valor = {segundo_valor}. ')