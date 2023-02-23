for i in range(10): #A ideia de while e For meio que trabalho de maneira igual, continue, break, etc...
    if i == 2:      #A maior diferença é que no while nao sabemos o numero de interações e no For sabemos quantas são.
        print('i é 2, pulando...')
        continue

    if i == 8: # Da mesma forma que foi feito no while. ao passar pelo break ele nao ira executar o else.
        print('i é 8, seu else não executará')
        break 

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso!')