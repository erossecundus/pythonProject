'''
Escreva um programa que permaneça em laço lendo números inteiros. O laço termina
quando for digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado
em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos.
Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela.
Ao final exiba a lista e a quantidade de elementos que ela contém.
---
Altere a solução ex.resolvido 7.6 de modo que todos os valores repetidos rejeitados sejam
incluídos em uma segunda lista. Ao final exiba essa segunda lista juntamente com seu tamanho.
'''

val = int(input('Digite um inteiro: '))
List = []
ListRejeitados = []
while val != 0:
    if val not in List:
        List.append(val)
    else:
        ListRejeitados.append(val)
    val = int(input('Digite um inteiro: '))
print(f'\nA lista contem {len(List)} valores:\n{List}')
print(f'\nA lista de rejeitados contem {len(ListRejeitados)} valores:\n{ListRejeitados}')
print('\nFim do programa')