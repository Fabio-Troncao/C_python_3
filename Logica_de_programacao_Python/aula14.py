a = 'A'
b = 'B'
c = 1.1

# Erro out of range for positional args tuple - Esta boscando anlgo que ja acabou.
#string = 'a={} b={} c={:.2f} {}'
string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

