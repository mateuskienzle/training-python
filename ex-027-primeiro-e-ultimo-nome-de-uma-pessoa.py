n = str(input('Digite seu nome completo:'))
nome = n.split()
print('Muito prazer em te conhecer!')
primeiro_nome = nome[0]
print('Seu primeiro nome é {}' .format(primeiro_nome))
ultimo_nome = (nome[len(nome)-1])
print('Seu ultimo nome é {}' .format(ultimo_nome))


'''Atenção!
Existe diferenças no formato em que o vscode lê as funções:
- len(nome)
- (nome[len(nome)-1])

no primeiro caso, como só esta sendo pedido pra informar o comprimento do texto, o codigo será lido da forma
natural (começando a contar a partir do 1), ou seja, se eu escrever "abacaxi está azedo" será retornado o 
numero exato do comprimento do texto digitado, nesse caso é 3.  
obs: é 3 pq, nesse exercicio, estou usando
o split() no inicio do codigo, atribuindo-o para todo o codigo. Desta forma, as posições são separadas entre
palavras, e nao letras.

no segundo caso, está sendo pedido para a variavel nome ser lida na posição informada entre os colchetes, nesse
caso é informado para ser lida no comprimento do texto da variavel nome (len(nome)) menos 1. O motivo do menos
1 (e é aqui que está a diferença entre a forma que o vscode lê as funções) é que, quando eu informo a posição
exata para ser lida (colocando informações entre colchetes ao lado da variavel nome) o código é lido da forma
não natural (começando a contar a partir do 0). Desta forma, se eu quero que o vscode leia a ultima palavra
do meu texto, eu preciso colocar o menos 1, porque como ele lê a partir do 0, a minha ultima palavra vai estar
uma posição a menos que do que ela seria se fosse contada da forma natural.'''


