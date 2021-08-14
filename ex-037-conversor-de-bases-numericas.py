numero_inteiro = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opçao = int(input('Sua opção: '))
if opçao == 1:
   binario = bin(numero_inteiro)
   print('{} convertido para BINÁRIO é igual a: {}' .format(numero_inteiro, binario[2:]))
elif opçao == 2:
   octal = oct(numero_inteiro)
   print('{} convetido para OCTAL é igual a: {}' .format(numero_inteiro, octal)[2:])
elif opçao == 3:
   hexa = hex(numero_inteiro)
   print('{} convertido para HEXADECIMAL é igual a: {}' .format(numero_inteiro, hexa)[2:])
else:
    print('Opção invalida.')

'''[2:] significa que estou solicitando ao programa que ele só mostre o resultado a partir do terceiro digito
do resultado. Desta forma, ele não irá mostrar os dois primeiros digitos, porque esses dois primeiros digitos
servem somente pra mostrar o tipo de base em que o número foi convertido'''
