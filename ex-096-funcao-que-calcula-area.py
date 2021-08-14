def area(larg, alt):
    a = larg * alt
    print(f'A área de um terreno de {larg} x {alt} é de {a}m²')

print('Controle de terrenos')
print('-' *20)
l = float(input('largura (m): ')) 
h = float(input('altura (m): '))  
area(l, h)