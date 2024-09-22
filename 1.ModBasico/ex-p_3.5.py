tempo = int(input('entre o tempo em segundos: '))
h = tempo//3600
h = f'{h} horas'
m = (tempo%3600)//60
s = (tempo%3600)%60
print(h, f'{m} minutos, {s} segundos', sep=', ')