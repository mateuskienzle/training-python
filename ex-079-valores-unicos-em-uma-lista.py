valores = list()
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não será adicionado...')
    pergunta = str(input('Quer continuar [S/N]? ')).upper()[0]
    if pergunta == 'N':
        break
print('=-' *30)
valores.sort()
print(f'Você digitou os valores {valores}')