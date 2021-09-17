# 5 pag por min
# 1 pag por 12 seg
qpag = int(input('Entre com o número de páginas da enciclopédia: '))
qt = qpag * 12
qh = qt // 3600
resto = qt % 3600
qm = resto // 60
qs = resto % 60
print(f'Tempo horas: {qh}')
print(f'Tempo minutos: {qm}')
print(f'Tempo segundos: {qs}')