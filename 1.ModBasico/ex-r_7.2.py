P = int(input('Entre o primeiro termo P: '))
R = int(input('Entre a razao R: '))
Q = int(input('Entre a quantidade Q de termos da p.a.: '))

ultimo = P+R*(Q-1)
print(f'lista resultante: ', list(range(P, ultimo+1, R)))