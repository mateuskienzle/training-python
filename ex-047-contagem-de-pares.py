for c in range(1, 51):
    if (c%2 == 0):
        print(c, end=' ')  
print('Acabou')

'''Outra forma de escrever esse código, de um modo que usasse menos processamento do computador, seria:
for n in range (2, 51, 2):
    print(n, end=' ')
print ('Acabou')

Desta forma, o código iria selecionar somente os números pares, sem precisar ler todos os números de 1 a 51 
(incluindo os numeros impares). Por conta disso, o processador seria menos utilizado e o programa seria mais 
"leve", visto que quando o código é feito da primeira forma mostrada aqui, o programa necessita ler todos
os números de 1 a 51 e, a partir dessa leitura, ele vai deixando de lado os números impares e printa somente
os numeros pares. Porém, dessa forma, exige-se mais processamento'''