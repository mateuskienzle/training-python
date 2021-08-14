peso = float(input('Qual é o seu peso (em Kg)? '))
altura = float(input('Qual é a sua altura (em m)? '))
imc = peso/(altura**2)
if imc < 18.5:
    estado = 'peso abaixo do normal, cuidado!'
elif 18.5 <= imc <= 24.9:
    estado = 'peso ideal, boa!'
elif 25 <= imc <= 29.9:
    estado = 'sobrepeso, cuidado!'
elif 30 <= imc <= 34.9:
    estado = 'obesidade grau um, tenha muito cuidado!'
elif 35 <= imc <= 39.9:
    estado = 'obesidade grau dois, tenha muito cuidado!'
else:
    estado = 'obesidade mórbida, tenha muito cuidado!'
print('O IMC dessa pessoa é de: {:.1f}' .format(imc))
print('Você está com {}' .format(estado))
