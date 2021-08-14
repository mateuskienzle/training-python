a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
b = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
c = a + b
while True:
    n = int(input('Digite um número ede 0 a 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('O número deve ser de 0 a 20 apenas. Tente novamente.') 
print(f'Você digitou o número {(c[n])}.')