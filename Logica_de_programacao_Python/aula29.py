"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
# em baixo temos um exemplo basico de erro. onde se tenta converter "a" para int.
"""
print(1234)
print(456)
int('a')
"""

numero_str = input(
    'Vou lhe dobrar o número que digitar: '
)

# com try: na primeira linha que der o erro ele ja passa para o except:
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um numero.')

# codigo abaixo para determinar se é numero mas ao usar 2.2 não resolve.
# No caso como topico dessa aula, veemos tambem que o if nao trata erros e nao é isso que queremos por agora.
"""if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Isso não é um numero.')"""
