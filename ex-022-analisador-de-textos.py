nome = str(input('Digite o seu nome completo:'))
print('Analisando seu nome...')
maiuscula = nome.upper()
minuscula = nome.lower()
letras = len(nome) - nome.count(' ')
primeiro = nome.split()
letras_primeiro = nome.find(' ')
print('Seu nome em letras maiúsculas é {} ' .format(maiuscula))
print('Seu nome em letras minúsculas é {}' .format(minuscula))
print('Seu nome tem ao todo {} letras' .format(letras))
print('Seu primeiro nome é {} e ele tem {} letras' .format(primeiro[0], letras_primeiro))