#Crear un programa que pida la distancia en metros
#y muestre un menu para convertir a kilometros o centimetros

distancia=float(input('Ingrese la distancia en metros: '))
opcion=input('Escoja la opcion a convertir\n'
            'a. convertir a kilometros\n'
            'b. convertir a centimetros\n')

if opcion.upper()=='A':
    resultado=distancia/1000
    print(f'La distancia en kilometros es {round(resultado,0)}')
elif opcion.upper()=='B':
    resultado=distancia*100
    print(f'La distancia en metros es {round(resultado,0)}')
else:
    print('ERROR')

