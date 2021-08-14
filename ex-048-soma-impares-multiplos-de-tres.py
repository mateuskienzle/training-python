soma = 0
contador = 0
for c in range(3, 501, 2):
    if (c%3 == 0):
        soma = soma + c
        contador = contador + 1
print('A soma de todos os {} valores solicitados é: {}' .format(contador, soma))

''' Uma forma de abreviar "soma = soma + c" seria colocando apenas "soma += c". O mesmo vale pro caso do
"contador", que ficaria "contador += 1"'''