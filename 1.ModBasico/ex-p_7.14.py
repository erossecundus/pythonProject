'''
Escreva um programa que leia um número inteiro nA e gere uma lista A com nA valores inteiros
aleatórios, não repetidos e situados na faixa [1, 100]. Mostre-a na tela em ordem crescente.
Em seguida leia outro inteiro nB e gere a lista B usando as mesmas regras aplicadas à lista A.
Mostre-a na tela também em ordem crescente.
Crie e exiba uma lista contendo a união das listas A e B, sem conter valores repetidos.
Mostre a lista resultante e a quantidade de elementos dela.
ex:
nA = 7    lista A = [8, 12, 29, 35, 44, 64, 81]
nB = 5    lista B = [10, 25, 35, 38, 64]
saida:
União de A e B
[8, 10, 12, 25, 29, 35, 38, 44, 64, 81] contém 10 elementos
'''
from random import randint
A = []
B = []
nA = int(input('Digite nA: '))
for i in range(nA):
    while True:
        x = randint(1,100)
        if A.count(x) == 0:
            A.append(x)
            break
A.sort()
print(f'Lista A = {A}')

nB = int(input('Digite nB: '))
for i in range(nB):
    while True:
        x = randint(1,100)
        if B.count(x) == 0:
            B.append(x)
            break
B.sort()
print(f'Lista B = {B}')

C = A + B
i = 0
while i < len(C):
    if C.count(C[i]) > 1:
        C.remove(C[i])
    i += 1
C.sort()
print(f'Uniao de A e B\n{C} contém {len(C)} elementos')
