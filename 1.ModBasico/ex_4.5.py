ph = float(input('entre o ph: '))
if ph < 6:
    r = 'ácido'
elif ph < 7:
    r = 'levemente ácido'
elif ph == 7:
    r = 'neutro'
elif ph < 8:
    r = 'levemente alcalino'
else:
    r = 'alcalino'
print(f'a solução de pH {ph} é {r}')
