moeda = input('qual moeda: ')
val = float(input('qual valor: '))

if moeda == 'D':
    val *= 4.89
elif moeda == 'E':
    val *= 5.26
elif moeda == 'L':
    val *= 6.17
else:
    val = ''
if val:
    print('R$ {:.2f}'.format(val))
else:
    print('moeda inválida')