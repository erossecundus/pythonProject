'''
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade
de números inteiros aleatórios quaisquer. Exiba a lista na tela.
Em seguida verifique se existem e elimine valores que estiverem repetidos, deixando apenas uma
ocorrência de cada. A ordem relativa dos elementos na lista não deve ser alterada, com exceção às
consequências da eliminação dos repetidos. Exiba a nova lista sem repetidos e o seu tamanho.

'''
from random import randint
qtde = int(input('Digite um valor inteiro: '))
l = []
for i in range(qtde):
    a = randint(1,10)
    l.append(a)
print(f'     lista: {l}')

tamanho = len(l)
i = 0
while i < tamanho:
    item = l[i]
    #print(f' {l[i]}')
    cont = l.count(item)
    while cont > 1:
        l.remove(item)
        cont -= 1
        tamanho -=1
    i += 1

print(f'nova lista: {l}')

