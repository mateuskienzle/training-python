matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior_valor = soma_colunas = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz[linha][coluna]= int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
        if matriz[linha][coluna]%2 == 0 :
            pares += matriz[linha][coluna]
print('=-'*30)
for linha in range(0, 3):
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]:^5}]' , end='')

    print()
print('=-' *30)
print(f'A soma dos valores pares é {pares}.')
for linha in range (0, 3):
    soma_colunas += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_colunas}.')
for coluna in range(0, 3):
    if coluna == 0:
        maior_valor = matriz [1][coluna]
    elif matriz[1][coluna] > maior_valor:
        maior_valor = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior_valor}.')