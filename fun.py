#Escribir una funcion que reciba N numeros, los cuales representan
#la puntuacion de un concurso, y esta devuelve la puntuacion del subcampeon.
#(ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)

ranking=[]
cantidadConcursantes = int(input('Ingrese la cantidad de participantes: '))
i=0
while i < cantidadConcursantes:
    i+=1
    participantes= float(input('Ingrese su puntuación: '))
    ranking.append(participantes)
print(ranking)
ranking.sort()
print(ranking)
print(ranking[-2])


