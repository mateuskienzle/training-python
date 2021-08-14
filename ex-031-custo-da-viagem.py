distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}km' .format(distancia))
valor_1 = (0.45*distancia)
valor_2 = (0.50*distancia)
if distancia >200:
    print('E o preço da sua passagem será de R${:.2f}' .format(valor_1))
else:
    print('E o preço da sua passagem será de R${:.2f}' .format(valor_2))