frase = str(input('Digite uma frase: ')).strip().lower()
a = (frase.count("a"))
print('A letra "a" aparece {} vezes na frase.' .format(a))
primeiro_a = (frase.find('a')+1)
print('A primeira letra "a" apareceu na posição {}' .format(primeiro_a))
ultimo_a = (frase.rfind('a')+1)
print('A ultima letra "a" apareceu na posição {}' .format(ultimo_a))


'''lembrando: 
- a função .strip() elimina os espaços antes e depois do texto digitado.
- a função .lower() colocada na mesma linha da variavel frase já faz com que o vs code, na hora de ler o codigo,
leia tudo em minusculo.
- a função frase.rfind procura a substring desejada da direita para esquerda.'''