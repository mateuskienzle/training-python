l=float(input('Largura da parede:'))
a=float(input('Altura da parede:'))
ar= l*a
t= ar/2
print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.3f}m².' .format(l, a, ar))
print('Para pintar essa parede, você precisará de {:.4f}l de tinta.' . format(t))