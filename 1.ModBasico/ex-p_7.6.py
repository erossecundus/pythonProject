'''
Escreva um programa que leia um número inteiro N. Em seguida leia N números inteiros
carregando os valores negativos em uma lista e os positivos em outra. Ao final
exiba na tela cada uma das listas juntamente como seu tamanho.
obs. Se o valor zero for fornecido ele deve ser incluído na lista de positivos.
---
Altere a solução ex.resolvido 7.4 para exibir as listas em ordem crescente
'''

N = int(input('Entre a quantidade N: '))
Lpos = []
Lneg = []
for i in range(N):
    x = int(input(f'entre o {i+1} o elemento: '))
    if x >= 0:
        Lpos.append(x)
    else:
        Lneg.append(x)
Lpos.sort()
Lneg.sort()
print(f'\n{len(Lpos)} positivos:\n{Lpos}')
print(f'\n{len(Lneg)} negativos:\n{Lneg}')
print('Fim do programa')

