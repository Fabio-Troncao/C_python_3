# Operadores lógicos
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia
# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# (entrada == 'E' or entrada == 'e') entre aspas para priorizar.

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
elif (entrada == 'S' or entrada == 's') and senha_digitada == senha_permitida:
    print('Sair')
else:
    print('Opçao nao escolhida ou senha errada')

# Avaliação de curto circuito

print(True and 0 and True)

senha = input('Senha: ') or 'Sem senha'
print(senha)