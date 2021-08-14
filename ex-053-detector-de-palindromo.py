frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print('O inverso de {} é {}.' .format(junto, inverso))
if inverso == junto:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')