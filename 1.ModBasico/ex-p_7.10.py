'''
Escreva um programa que leia um número inteiro Qtde e carregue uma lista com essa quantidade de números inteiros
aleatórios entre 1 e 100. Exiba a lista na tela. Em seguida inicie um laço que deve permanecer em execução
enquanto um valor inteiro X for maior que zero. Para cada valor de X verifique se ele está na lista gerada
e caso esteja elimine-o. Se houver mais de uma ocorrência de X na lista, elimine todas.
Após as eliminações exiba a lista novamente.
'''
from random import randint
qtde = int(input('Digite um inteiro: '))
lista =[]
for i in range(qtde):
    lista.append(randint(1,100))
while True:
    print(lista)
    x = int(input('Digite um inteiro para remover: '))
    if x == 0:
        break
    else:
        while lista.count(x) > 0:
            lista.remove(x)
print('fim do programa')
