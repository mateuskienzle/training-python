sexo = str(input('Informe o seu sexo [M/F/N] (M = Masculino; F = Feminino; N = Nenhum): ')).strip().upper()[0]
while (sexo not in 'MFN'):
    sexo = str(input('Dados inválidos. Por favor, digite novamente o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!' .format(sexo))