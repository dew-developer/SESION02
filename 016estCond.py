#El programa debe pedir una cantidad en pesos
#y mostrar un menu de opciones para convertirlo a 
#dolares americanos o soles
pesos=float(input('Ingresa la cantidad de pesos'))
opcion=int(input('\nIngrese la moneda a la que desea convertir\n'
                 '1. Convertir a soles 5$\n'
                 '2. Convertir a dolares 21$\n'))

if(opcion==1):
    total=pesos/5
    print(f'El total de soles es {round(total)}')
elif opcion==2:
    total=pesos/21
    print(f'El total de dodlares es {round(total)}')
else:
    print('Esa opcion no existe')


                