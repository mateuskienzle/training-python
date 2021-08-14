from datetime import date
ano_nascimento = int(input('Ano de nascimento: '))
idade = (date.today().year - ano_nascimento)
print('O atleta tem {} anos' .format(idade))
if idade <= 9:
    classificacao = 'MIRIM'
elif 9 < idade <=14:
    classificacao = 'INFANTIL'
elif 14 < idade <= 19:
    classificacao = 'JUNIOR'
elif 19 < idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'
print('Classificação: {}.' .format(classificacao))