'''
Escreva um programa que leia um número inteiro N. Em seguida leia N números reais
carregando-os em uma lista. Ao final exiba os elementos da lista na tela, sendo um em cada linha
---
Altere a solução do ex.resolvido 7.3 para exibir os números reais da lista com duas casas decimais.
---
Altere a solução do ex.resolvido 7.3 incluindo o comando try-except na leitura dos números reais
para evitar a digitação incorreta dos valores.
Quando ocorrer uma exceção uma mensagem deve ser exibida na tela informando esta condição.
---
Altere a solução do ex.resolvido 7.3 para exibir os resultados em ordem inversa à ordem de leitura
'''

N = int(input('Digite a quantidade N: '))
L = []
for i in range(N):
    try:
        x = float(input(f'  elemento {i}: '))
        L.append(x)
    except ValueError:
        print('Valor inválido, digite um real!')
L.reverse()
print('\nResultado')
for valor in L:
    print(f'  {valor:.2f}')
print('Fim do programa')