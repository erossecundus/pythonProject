a = float(input('primeiro lado: '))
b = float(input('segundo lado: '))
c = float(input('terceiro lado: '))

if a > 0 and b > 0 and c > 0:
    if a > b:
        aux = a
        a = b
        b = aux
    if b > c:
        aux = b
        b = c
        c = aux
    if a + b <= c:
        msg = f'{a}, {b} e {c} não formam um triângulo'
    else:
        if a == b and a == c and b == c:
            msg = f'{a}, {b} e {c} formam um triângulo equilátero'
        elif a == b or a == c or c == b:
            msg = f'{a}, {b} e {c} formam um triângulo isosceles'
        else:
            msg = f'{a}, {b} e {c} formam um triângulo escaleno'
else:
    msg = f'{a}, {b} e {c} precisam ser maiores que zero'

print(msg)