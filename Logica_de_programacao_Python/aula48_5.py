"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Fábio') # Aqui o append ira estender a lista com algum valor. mas nao da para passar esse conteudo para uma variavel.
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5) # unsando o insert irei passar 2 argumentos. O primeiro é o indice e o segundo é o valor a inserir. 
#Obs: o Um indice grande nao quer dizer que ele vai para essa posição, mas sim para a ultima posição, caso o indice seja maior que o ultimo da lista.
print(lista[4]) # obs: Tentar printar algo fora da lista ele ira dar erro.
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
lista_1.append(lista_2)
print(lista_1)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Fabio', 'Maria', 1, True, 1.2]
#lista_b = lista_a # se fizer isso Lista_b vai copiar a lista do endereço de memoria ou seja:
# se alterar algum valor de lista_a e printar lista_b a mesma ira ter o valor diferente. obs: testarem para ver essa interação ;)
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)