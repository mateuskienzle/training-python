n=input('Digite um valor:')
print(type(n))
print('É um numero:', n.isnumeric())
print('É alfabetico:', n.isalpha())
print('É alfanumerico:', n.isalnum())
print('Só tem espaços:', n.isspace())
print('Todos caracteres minusculos:', n.islower())
print('Todos caracteres maiusculos:', n.isupper())
print('Aceita perimetros:', n.isprintable())
print('Está captalizada:', n.istitle())