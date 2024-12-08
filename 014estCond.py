#El programa evalua la estatura
#Si tu estatura es menor a 160cm imprimira: Eres de estatura baja
#Si tu estatura esta entre 160 y 175 imprimira: Eres estatura mediana
#Si tu estatura es mayor a 175cm imprimira: Eres de estatura alta

nombre=input('Escribe tu nombre: ')
estatura=float(input('Escribe tu estatura: '))

if(estatura<160 and estatura>20):
    print(f'{nombre} eres de estatura baja')
elif(estatura>=160 and estatura <=175):
    print(f'{nombre} tu estatura es normal')
elif (estatura>175 and estatura<230):
    print(f'{nombre}  tu estatura es alta  ')
else:
    print(f'{nombre} esa estatura no es valida')
        

