f = int(input('entre um inteiro: '))
prim = int(input('entre prim: '))
i = 1
t1, t2 = 0, 1
qtde = 0
seq = 'sequencia menor que prim: '
while i <= f:
    if i == 1:
        termo = 0
    elif i == 2:
        termo = 1
    else:
        termo = t1 + t2
        t1 = t2
        t2 = termo
    print(f'{termo}', end=' ')
    i += 1

    if termo > prim:
        qtde += 1
        seq += f'{termo} '

print(f'\nqtde: {qtde}')
print(seq)