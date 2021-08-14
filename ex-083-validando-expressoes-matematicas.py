parenteses_aberto = list()
parenteses_fechado = list()
expressao = str(input('Digite a expressão: '))
for parenteses in expressao:
    if parenteses == '(':
        parenteses_aberto.append('(')
    if parenteses == ')':
        parenteses_fechado.append(')')
if len(parenteses_aberto) == len(parenteses_fechado):
    print('Expressão válida!')
else:
    print('Expressão inválida!')