velocidade = int(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('\033[0:34:44m MULTADO! Você excedeu o limite de velocidade permitido que é de 80km/h!')
    print('Você deve pagar uma multa de R${:.2f}' .format (multa))
print('Tenha um bom dia! Dirija com segurança!')