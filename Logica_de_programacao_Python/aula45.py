"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
#texto_iter = 'Fábio'.__iter__() #O que vai printar <str_iterator object at 0x000002D85CD7AC20>
texto_iter = iter('Fábio') # Mesma coisa que linha anterior.
print(texto_iter) # Resumidamente É um objeto interador str que está nesse endereço de memoria.

# for letra in texto
texto = 'Fábio'  # iterável -> Pode se dizer que é o elemento que tem os elementos
"""print(texto_iter.__next__()) # Aqui dá para ter a ideia de como o for trabalha por traz dos panos, pois ele vai usando o next para passar os valores ate aparecer o erro StopIteration  
print(texto_iter.__next__())
print(texto_iter.__next__())
print(texto_iter.__next__())
print(texto_iter.__next__())
print(texto_iter.__next__())
print(' ')"""

"""iteratador = iter(texto)  # iterator

while True: #Isso aqui é uma ideia do que o for faz por traz dos panos.
    try:
        letra = next(iteratador) # Aqui iremos passar a letra do iterador com o next.
        print(letra)
    except StopIteration: # E aqui é o erro que o Python passa apos usar o next onde nao existe.
        break"""

for letra in texto:  # o que foi feito no while acima é a mesma coisa que o for está fazendo.
    print(letra)