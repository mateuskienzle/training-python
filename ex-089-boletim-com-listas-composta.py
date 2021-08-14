alunos = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    pergunta = str(input('Quer continuar [S/N]? ')).upper()[0]
    if pergunta == 'N':
        break
print('-=' *30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
print('-' *30)
for i, v in enumerate(alunos): 
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')
while True:
        print('-' *30)
        notas_aluno = int(input('Mostrar as notas de qual aluno? (Digite 999 para encerrar): '))
        if notas_aluno == 999:
            print('Fim do Boletim.')
            break
        if notas_aluno <= len(alunos)-1:
            print(f'As notas de {alunos[notas_aluno][0]} são {alunos[notas_aluno][1]}')