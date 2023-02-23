frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

#print(frase.count('Python')) # .count() contar quantas vezes apareceu algo na string.

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
#permitidos =  ' o' # Aqui fica um exemplo de como poderia fazer se em de verificar so um carectere, se eu fosse vereficar mais que 1. usando -> if letra_atual in permitidos:

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ': # Aqui irei retirar o espaço da contagem, mas irei colocar
        i += 1
        continue

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi o '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)