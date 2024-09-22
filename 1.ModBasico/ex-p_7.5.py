'''
Escreva um programa que leia um número inteiro N. Em seguida leia N números inteiros
carregando os valores negativos em uma lista e os positivos em outra. Ao final
exiba na tela cada uma das listas juntamente como seu tamanho.
obs. Se o valor zero for fornecido ele deve ser incluído na lista de positivos.
---
Responda a seguinte questão. A inicialização das listas foi feita da seguinte forma:
LstNeg = []  LstPos = []
por quê a solução 7.4 ficaria errada se a inicialização das listas fosse feita assim?
LstNeg = LstPos = []  Justifique sua resposta. >> Estaria atribuindo nomes diferentes para objetos de ID iguais
Dicas:
a) altere o programa do exercício resolvido 7.4 e teste para ver o que acontece;
b) releia as seções 2.3, 2.4 e 7.2.5
'''

N = int(input('Entre a quantidade N: '))
Lpos = Lneg = []

for i in range(N):
    x = int(input(f'entre o {i+1} o elemento: '))
    if x >= 0:
        Lpos.append(x)
    else:
        Lneg.append(x)
print(f'\n{len(Lpos)} positivos:\n{Lpos}')
print(f'\n{len(Lneg)} negativos:\n{Lneg}')
print('Fim do programa')

