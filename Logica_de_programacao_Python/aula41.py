""" while/else """

string = 'Valor qualquer' # com espaço executa o if e sai do laço. Sem o espaço termina o while e pega mensagem do else.

i = 0
while i < len(string):
    letra = string[i]

    #break # So para exemplo: Se dentro do while tiver um break, ele sai do laço e nao vai entrar no else e mostrar a mensagem.
    if letra == ' ': # Outro exemplo: fiz uma busca para saber se minha string contem espaço. Ao entrar no if pega o break e sai do laço sem entrar no else.
        break

    print(letra)
    i += 1
else:
    print('O else foi executado. Então nao encontrei um espaço na string. ')# Aqui o print irá ser executado apos o while terminar
print('Fora do while. ')# já este printe, está fora do while
