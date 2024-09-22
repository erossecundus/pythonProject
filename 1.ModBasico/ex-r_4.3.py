n1=int(input('primeiro numero: '))
n2=int(input('segundo numero: '))
if n1 < n2:
    msg = f'o numero {n1} é menor'
elif n1 > n2:
    msg = f'o numero {n2} é menor'
else:
    msg = f'os numeros são iguais e valem {n2}'
print(msg)