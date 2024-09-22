'''
Versao reduzida do exemplo do ebook
Testando match-case
'''
LL = int(input('Digite o código: '))
match LL:
    case 16:
        print('Bebe')
    case 23:
        print('Infantil')
    case 42:
        print('Masculino')
    case 52:
        print('Feminino')
    case _:
        print('Código inválido!')
