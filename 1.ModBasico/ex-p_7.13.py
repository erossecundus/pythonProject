'''
Escreva um programa que permaneça em laço lendo três dados de um produto:
o código (int), o preço de compra (float) e o preço de venda(float).
Com esses dados forme uma tupla e armazene-a em uma lista. Os três dados devem ser lidos
em uma única linha separados por espaço em branco. O laço termina quando forem digitados três zeros: 0 0 0
Em seguida, para todas as tuplas presentes na lista, exiba o código do produto e a margem bruta de lucro
do produto em porcentagem e com uma casa decimal.
A margem bruta de lucro é calculada com a expressão: 𝑀𝑎𝑟𝑔𝑒𝑚𝐵𝑟𝑢𝑡𝑎 = ( (𝑃𝑟𝑒ç𝑜 𝑉𝑒𝑛𝑑𝑎 /𝑃𝑟𝑒ç𝑜 𝑑𝑒 𝐶𝑜𝑚𝑝𝑡𝑎) −1 )*100%
'''

prod = []
print('Entre os valores para código, preço de compra e preço de venda:')
while True:
    item = input()
    t = (int(item.split()[0]), float(item.split()[1]), float(item.split()[2]))
    if t == (0, 0, 0):
        break
    else:
        prod.append(t)

for p in prod:
    margem = ((p[2]/p[1]) - 1) * 100
    print(f'Codigo: {p[0]} - Margem: {margem:.1f}')
