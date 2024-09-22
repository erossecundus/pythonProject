P = int(input('Entre o primeiro termo P: '))
R = int(input('Entre a razao R: '))
Q = int(input('Entre a quantidade Q de termos da p.a.: '))

L = []
i=0
while i < Q:
    L.append(P)
    P += R
    i += 1
print(f'lista resultante: {L}')