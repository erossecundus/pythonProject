v1 = input('entre o nome do vendedor 1: ')
vt1 = float(input('entre o valor total vendido pelo vendedor 1: '))
v2 = input('entre o nome do vendedor 2: ')
vt2 = float(input('entre o valor total vendido pelo vendedor 2: '))
v3 = input('entre o nome do vendedor 3: ')
vt3 = float(input('entre o valor total vendido pelo vendedor 3: '))

s1 = f'vendedor {v1} vendeu R${vt1} e recebe comissão de R$ {vt1*0.06:.2f}'
s2 = f'vendedor {v2} vendeu R${vt2} e recebe comissão de R$ {vt2*0.06:.2f}'
s3 = f'vendedor {v3} vendeu R${vt3} e recebe comissão de R$ {vt3*0.06:.2f}'

print(s1, s2, s3, sep='\n')
