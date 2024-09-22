# Trata TODOS os erros que podem ocorrer no exemplo anterior
try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(R)
except ZeroDivisionError:
    print('Nao é possivel dividir por zero!')
except ValueError:
    print('Digite um inteiro para A e B')
except:
    print('Não foi possível fazer a divisão')
print('Fim do programa')
