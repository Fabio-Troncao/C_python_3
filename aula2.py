# sep="-" mudar o separador 
# \r é um Carriage Return \n é um line feed
# \r\n -> CRLF = Carriage Return Line Feed
# end=' ' permite modificar o final ja predefenido trocando por outro caracter
print(12, 34, 1011, sep=" ", end='\r\n')
print(12, 34, 1011, sep=" ", end=' # ')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')