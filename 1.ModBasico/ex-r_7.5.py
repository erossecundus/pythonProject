'''
Escreva um programa que permaneça em laço lendo números inteiros.
O laço termina quando for digitado 0 (zero).
Cada valor diferente de zero digitado deve ser colocado em uma lista.
Ao final exiba a lista na tela e a quantidade de elementos que ela contém.
'''

val = int(input('Digite um inteiro: '))
List = []
while val != 0:
    List.append(val)
    val = int(input('Digite um inteiro: '))
print(f'\nA lista contem {len(List)} valores:\n{List}')
print('\nFim do programa')
