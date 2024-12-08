#El programa debe calcular el promedio de las calificaciones
#del alumno e informarle si esta aprobado o desaprobado
print('El programa calcula el promedio y determina si estas aprobado o no')
nombre=input('Escribe tu nombre')
mat=float(input('Escribe tu calificacion de mat'))
fis=float(input('Escribe tu calificacion de fisica'))
quim=float(input('Escribe tu calificacion de quimica'))
promedio=(mat+fis+quim)/3
if(promedio>=11):
    print(f'{nombre} tu promedio es: {promedio}, estas aprobado')
else:
    print(f'{nombre} tu promedio es: {promedio}, estas desaprobado')
