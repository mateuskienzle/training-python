from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('    [ 1 ] Somar')
    print('    [ 2 ] Multiplicar')
    print('    [ 3 ] Maior')
    print('    [ 4 ] Novos números')
    print('    [ 5 ] Sair do programa')
    opcao = int(input('>>> Qual é a sua opção? ' ))
    if opcao == 1:
        soma = (n1 + n2)
        print('A soma entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = (n1*n2)
        print('A multiplicação entre {:.1f} e {:.1f} é igual a {:.1f}' .format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 == n2:
            print('Os valores {:.1f} e {:.1f} são idênticos. Portanto, não há maior.' .format(n1, n2))
        else:
            maior = max(n1, n2)
            print('O maior valor entre {:.1f} e {:.1f} é {:.1f}' .format (n1, n2, maior))
    elif opcao == 4:
        print('Informe os número novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente:')
    print('-=' *20)    
    sleep(2)
print('Fim do programa!')