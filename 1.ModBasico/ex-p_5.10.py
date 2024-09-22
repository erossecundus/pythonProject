p = int(input('entre um numero: '))
i = 2
msg = f'{p} é primo'
r = p//2+1
while i < r:
    if p%i == 0:
        msg = f'{p} não é primo - divide por {i}'
        break
    i += 1
print(msg)
