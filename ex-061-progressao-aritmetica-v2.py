print('Gerador de PA')
print('-=' *10)
n = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
soma = n
while c <= 10:
    print('{}' .format(soma), end=' -> ')
    soma += r
    c += 1
print('FIM')

''' eu poderia ter declarado minha variavel de contador igual a 0 em vez de igual a 1 ("c=1"). Porém, 
no while eu teria que por "while c < 10", sem o igual "=" antes do 10.'''