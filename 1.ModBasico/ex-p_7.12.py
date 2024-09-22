'''
Escreva um programa que permaneça em laço de modo que em cada repetição seja lido e
armazenado em uma lista o nome de uma pessoa. O laço termina quando o usuário entrar com um string vazio.
Exiba na tela a lista de nomes em ordem alfabética e precedida de um número de ordem começando em 1.
Exemplo:
1 Bernardo Almeida
2 Carlos Eduardo Soares
3 Julia Monteiro da Silva
4 Margarete Guimarães
5 Robson de Souza Andrade
'''

nomes = []
i = 1
while True:
    nome = input(f'Digite o {i}o nome: ')
    if nome:
        nomes.append(nome)
    else:
        break
    i += 1
for n in range(len(nomes)):
    print(f'{n+1} {nomes[n]}')
