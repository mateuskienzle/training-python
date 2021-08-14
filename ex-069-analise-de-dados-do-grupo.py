c = homens = mulheres_menos_20 = 0
while True:
    print('-' *35)
    print('\tCADASTRE UMA PESSOA')
    print('-' *35)
    idade = int(input('Idade: '))
    sexo =  ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' *35)
    if idade >= 18:
        c += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
            mulheres_menos_20 += 1
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar [S/N]? ')).upper()[0]
    if pergunta == 'N':
        print('-' *35)
        print(f'Total de pessoas com mais de 18 anos: {c}')
        print(f'Ao todo temos {homens} homens cadastrados.')
        print(f'E temos {mulheres_menos_20} mulheres com menos de 20 anos.')
        break

    ''' NESSA EU FUI BRABÍSSIMO E RAPIDÍSSIMO!!!!
    
    OBS: O "\t" utilizado no campo print = ('\tCADASTRE UMA PESSOA') serve para centralizar o texto desse
    print.'''