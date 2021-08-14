soma = 0 
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: ' .format(c)))
    if (n%2==0):
        soma = soma + n
        cont = cont + 1
if soma == 0:
    print('Você não informou nenhum número par, portanto a soma é igual a zero.')
else:
    if cont == 1:
        print('Como você só digitou {} número par, a soma é igual ao próprio número: {}' .format(cont, soma))
    else:
        print('A soma dos {} números pares inseridos é: {}' .format(cont, soma))