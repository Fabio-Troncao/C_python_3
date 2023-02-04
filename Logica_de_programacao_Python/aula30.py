"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

# Colocando tudo maiusculo deixa as variaveis constantes, ou seja conteudo que nunca ira mudar em todo o programa.
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

#DICA: Para trocar nome de uma mesma variavel repetida, basta selecionar ela e precionar F2 pois modificando a mesma ela ira ser trocada em todo codigo.
# uma ideia ou exemplo de como criar condiçoes em variaveis. Para simplificar e deixar codigo mais limpo.
velocidade_carro_passou_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')

# na linha abaixo usei a \ invertida so para fazer uma troca de linha. Pois usando \ estou informando ao python que a linha tem continuação.
# Ideia abaixo seria em saber e mostrar printe caso velocidade seja acima de RADAR_1 entre o LOCAL_1 entre um RANGE de +- LOCAL_1
"""if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('Carro multado em radar 1')"""

#Simplificando codigo das linhas anteriores. Deixando ele mais CLEAN!

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')
