word = ' Cálculo de metros '
print(f'{word:=^40}')

dist = float(input('Digite uma distância: '))

km = dist * 0.001
hm = dist * 0.01
dam = dist * 0.1
dm = dist * 1
cm = dist * 10
mm = dist * 100

print(f'A medida de {dist} corresponde a: {km} km')
print(f'A medida de {dist} corresponde a: {hm} hm')
print(f'A medida de {dist} corresponde a: {dam:.1f} dam')
print(f'A medida de {dist} corresponde a: {dm:.0f} dm')
print(f'A medida de {dist} corresponde a: {cm:.0f} cm')
print(f'A medida de {dist} corresponde a: {mm:.0f} mm')
    
    






