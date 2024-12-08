#sumatoria de numeros, cuando presionamos 0 salimos

suma=0
numero=9

while numero!=0:
    numero=int(input('ingresa el numero: \n'))
    suma+=numero

print(f'la sumatoria es {suma}')
