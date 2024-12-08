#El programa debe pedir el numero de dia
#que el trabajador quiere horas extras y avisarle cual dia trabajara

nombre=input('Escribe tu nombre')
dia=int(input('escribe el numero de dia que quieres trabajar horas extra'))

if dia==1:
    print(f'{nombre} tendras horas extra el dia Lunes')
elif dia==2:
    print(f'{nombre} tendras horas extra el dia Martes ')
elif dia==3:
    print (f'{nombre} tendras horas extra el dia Miercoles')
elif dia==4:
    print(f'{nombre} tendras horas extra el dia jueves')
elif dia==5:
    print(f'{nombre} tendras horas extra el dia vierners')
elif dia==6:
    print(f'{nombre} tendras horas extra el dia Sabado')
elif dia ==7:
    print(f'{nombre}El domingo se descansa')
else :
    print(f'{nombre} ese dia no es valido')