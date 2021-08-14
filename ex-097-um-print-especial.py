def texto(frase):
    tamanho_frase = len(frase) +4
    print('~' * tamanho_frase)
    print(f' {frase}')
    print('~' * tamanho_frase)
    
frase_personalizada = str(input('Escreva uma frase: '))
texto(frase_personalizada)

'''hello'''