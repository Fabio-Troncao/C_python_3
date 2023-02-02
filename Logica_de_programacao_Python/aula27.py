"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:8])
print(len(variavel[4:8])) # len() pegar tamanho

#Fatiamento

print(variavel[0:9:1]) #Inicia no 0: o numero de caracteres 9: de 1 em 1
print(variavel[0:len(variavel):2]) #Inicia no 0: usando len() para o numero de caracteres 9: de 2 em 2
print(variavel[-1:-10:-1]) #Negativo: Inicia no -1: o numero de caracteres -10: de -1 em -1 mas para traz ou inverso. OBS todos campos negativos.
print(variavel[::-1]) #Negativo: Dessa forma so inverte.


