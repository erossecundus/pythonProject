'''
Escreva um programa que leia um número inteiro Qtde e carregue uma lista
com essa quantidade de números inteiros aleatórios. Exiba a lista na tela.
Em seguida inicie um laço que deve permanecer em execução enquanto um valor inteiro X for maior que zero.
Para cada valor de X verifique se ele está ou não na lista gerada.
Caso esteja é preciso exibir a quantidade de ocorrências.
'''

from random import randint

Qtde = int(input('Digite a quantidade: '))
List = []
# Primeira parte: Gerando a lista
for i in range(Qtde):
    List.append(randint(1,20))
print(f'\nLista gerada:\n{List}')

# Segunda parte: Pesquisa na lista
x = 1
while x > 0:
    x = int(input('Digite um valor: '))
    List.count(x)
    if x in List:
        print(f'   Há {List.count(x)} repetições do elemento {x} na lista.')
    else:
        print(f'{x} nao esta na lista')
print('fim do programa')