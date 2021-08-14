valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos_financiamento = int(input('Quantos anos de financiamento?'))
prestacao = valor_casa/(anos_financiamento*12)
print('Para pagar uma casa de R${:.2f} em {:.2f} anos, a prestação será de R$ {:.2f}' .format(valor_casa, anos_financiamento, prestacao))
if prestacao > 0.3*salario:
   print('Empréstimo NEGADO!')
else: 
    print('Empréstimo ACEITO! Parabéns!')
