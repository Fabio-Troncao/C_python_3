# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
elif entrada == 'S' and senha_digitada == senha_permitida:
    print('Sair')
else:
    print('Nenhuma das alternativas escolhidas ou senha errada.')

# Avaliação de curto circuito
# bool(0) == False
# bool(1) == True
# Outro Exemplo
# bool('') string vazia == False
# bool(' ') string nao vazia == True
#print(bool(''))

#print(True and False and True)
#print(True and 0 and True)