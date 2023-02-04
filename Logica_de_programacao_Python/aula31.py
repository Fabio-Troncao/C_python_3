"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
# Busca Valor na memoria, usando ID se pode observar.
"""
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))
"""
condicao = True
#criar variavel para confirmação de entrada em if utilisando 'None'
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
# No caso debaixo como o passou_no_if entrou no IF ele nao vai ser mais None, pois dentro do IF temos 'passou_no_if = True'
print(passou_no_if, passou_no_if is None)
# Na linha abaixo estamos perguntando se ele nao é mais None. Ai ele vai ser True pois ele entrou no If o mesmo foi modificado entao ele nao é mais None.
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')