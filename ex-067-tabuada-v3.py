while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n < 0:
        print('Programa tabuada encerrado.')
        break
    else:
       for c in range (1, 11):
            print(f'{n} x {c:2} = {n*c}')
    print('-'*20)