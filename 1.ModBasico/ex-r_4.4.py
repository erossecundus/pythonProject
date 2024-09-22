nome = input('entre o nome: ')
peso = float(input('entre o peso: '))

if peso < 52:
    cat = ''
elif peso < 65:
    cat = 'pena'
elif peso < 72:
    cat = 'leve'
elif peso < 79:
    cat = 'ligeiro'
elif peso < 86:
    cat = 'meio-medio'
elif peso < 90:
    cat = 'medio'
elif peso < 100:
    cat = 'meio-pesado'
else:
    cat = 'pesado'
msg = 'o lutador {} pesa {:.3f} kg e se enquadra na categoria {}'
if cat != '':
    print(msg.format(nome,peso,cat))
else:
    print(f'peso inválido: {peso}')