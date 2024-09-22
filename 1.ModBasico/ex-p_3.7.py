inv = float(input('entre o investimento '))
custo = float(input('entre o custo '))
receita = float(input('entre a receita '))

roi = (receita-(custo+inv))/(custo+inv)

print(f'ROI = {roi*100:.1f}%')