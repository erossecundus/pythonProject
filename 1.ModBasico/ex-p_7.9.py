'''
Altere o programa do Exercício Proposto 7.8 acrescentando uma validação adicional
para garantir que a data fornecida seja válida. Por exemplo: a entrada 20242255 é
válida segundo os critérios estabelecidos no enunciado 7.8. Porém, 55/22/2024 não
é uma data válida. Neste exercício você deve garantir que a data seja válida
(incluindo anos bissextos – para identificar se um ano é bissexto veja o Exercício Proposto 4.8).

---
ex7.8:
Escreva um programa que leia um string contendo uma data no formato aaaammdd,
onde aaaa é o ano com 4 dígitos; mm é o mês com 2 dígitos; dd é o dia com 2 dígitos.
O programa deve validar a entrada verificando dois itens:
a) se foram fornecidos 8 caracteres;
b) se todos os caracteres são dígitos numéricos.
Se a entrada for válida o programa deve produzir a saída exemplificada abaixo;
    A data fornecida é: dd/mm/aaaa
se for inválida deve exibir uma mensagem de erro (que você pode elaborar como desejar).
'''

data = input('Forneça uma data no formato aaaammdd: ')
if len(data) == 8 and data.isnumeric():
    dia = int(data[6:])
    mes = int(data[4:6])
    ano = int(data[0:4])
    if mes in [1, 3, 5, 7, 8, 10, 12] and 1 <= dia <= 31:
        valid = True
    elif mes in [4, 6, 9, 11] and 1 <= dia <= 30:
        valid = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            if 1 <= dia <= 29:
                valid = True
            else:
                valid = False
        else:
            if 1 <= dia <= 28:
                valid = True
            else:
                valid = False
    else:
        valid = False

    if valid:
        print(f'A data fornecida é: {dia}/{mes}/{ano}')
    else:
        print('Data inválida!')
else:
    print('Data inválida!')
print('fim do programa')