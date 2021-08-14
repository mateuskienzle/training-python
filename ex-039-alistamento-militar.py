from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = (ano_atual-nascimento)
print('Quem nasceu em {} tem {} anos em {}.' .format(nascimento, idade, ano_atual))
if idade > 18:
    data_alistamento = (idade-18)
    ano_alistamento = (nascimento+18)
    if data_alistamento == 1:
        print('Você já deveria ter se alistado há {} ano.' .format(data_alistamento))
    elif data_alistamento > 1:
        print('Você já deveria ter se alistado há {} anos.' .format(data_alistamento))
    print('Seu alistamento foi em {}.' .format(ano_alistamento))
elif idade < 18:
    data_alistamento = (18-idade)
    ano_alistamento = (nascimento+18)
    if data_alistamento == 1:
        print('Você deverá se alistar daqui a {} ano' .format(data_alistamento))
    elif data_alistamento > 1:
        print('Você deverá se alistar daqui a {} anos' .format(data_alistamento))
    print('Seu alistamento será em {}' .format(ano_alistamento))
elif idade == 18:
    print('Você tem que se alistar imediatamente!')