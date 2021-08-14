n = int(input('Informe o número de pessoas que serão analisadas: '))
idade_total = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulher_menor_20 = 0
for pessoa in range (1 , n+1):
    print('---- {}ª PESSOA ----' .format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    idade_total += idade
    media = (idade_total/n)
    if sexo == 'M':
        if n == 1:
            maior_idade_homem = idade
            nome_homem_velho = nome
        else:
             if idade > maior_idade_homem:
                maior_idade_homem = idade
                nome_homem_velho = nome
    if sexo == 'F':
        if idade < 20:
            total_mulher_menor_20 += 1
print('A média de idade do grupo é de {:.1f} anos.' .format(media))
print('O homem mais velho tem {} anos e se chama {}.' .format(maior_idade_homem, nome_homem_velho))
if total_mulher_menor_20 == 1:
    print('Ao todo só tem {} mulher com menos de 20 anos.' .format(total_mulher_menor_20))
else:
    print('Ao todo são {} mulheres com menos de 20 anos.' .format(total_mulher_menor_20))