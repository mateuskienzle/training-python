n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do(a) aluno(a) é {:.1f}' .format(n1, n2, m))
if m >= 7:
    print('Aluno(a) APROVADO(A)!')
elif 5 <= m < 7:
    print('Aluno(a) está em RECUPERAÇÃO!')
else:
    print('Aluno(a) está REPOVADO(A)!')
