'''
Escreva um programa que leia um string contendo três números inteiros separados
por espaços em branco. Separe-os em objetos int, calcule sua soma e exiba na tela.
'''

val = input('Entre tres valores inteiros: ')
val = val.split()
for i in range(len(val)):
    val[i] = int(val[i])
    print(f'n1 = {val[i]}')
soma = sum(val)
print(soma)
print('fim do programa')