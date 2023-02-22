"""
Iterando strings com while
"""
#.......12345678910111213
nome = 'Fabio Troncao' # Iteráveis
#-1.13121110987654321

# Usar printe para confirmar, no caso de Duvida.
"""print(nome[-11]) # usando -11 por exemplo ele vai contar de frente para traz sendo o -11 = b

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*F*a*b*i*o* *T*r*o*n*c*a*o'"""

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)