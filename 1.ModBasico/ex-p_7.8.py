'''
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
    print(f'A data fornecida é: {data[6:]}/{data[4:6]}/{data[0:4]}')
else:
    print('Data inválida!')
print('fim do programa')