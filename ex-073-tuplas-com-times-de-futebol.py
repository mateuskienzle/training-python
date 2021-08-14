times = ('Corinthians', 'Plameiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 
         'Fluminense', 'Sport Recife', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' *20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' *20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' *20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' *20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' *20)
for pos, chapecoense in enumerate(times):
    if chapecoense == 'Chapecoense':
        print(f'O {chapecoense} está na {pos+1}ª posição')