from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:{}' . format(lista))


#duvida
'''Por que nesse exercicio eu nao posso atribuir uma variavel(ordem) que será igual ao comando "shuffle(lista)"
Aí na hora de printar, eu só informaria que o elemento que eu quero printar é essa variavel que se refere
ao suffle(lista)

Ficaria assim:

from random import shuffle
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
ordem = shuffle(lista)
print('A ordem de apresentação será:{}' . format(ordem))''' 