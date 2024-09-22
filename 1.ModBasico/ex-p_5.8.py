pInd = pRes = 0

while True:
    prod = int(input('entre o código: '))
    if prod == 0:
        break
    qtde = int(input('entre a quantidade: '))
    if prod//1000 == 1:
        pRes += qtde
    elif prod//1000 == 2:
        pInd += qtde
    else:
        print('tipo inválido!')
print(f'Residencial: {pRes} - Industrial: {pInd}')
