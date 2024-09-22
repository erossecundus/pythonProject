# Trata o erro de divisao de forma simples
A = int(input('Digite A: '))
B = int(input('Digite B: '))
try:
    R = A / B
    print(R)
except:
    print('Nao é possivel calcular a divisao!')
print('Fim do programa')
