#def evaluacion(nota):
#   valoracion="aprobado"
#    if nota <5:
#        valoracion="suspenso"
#    return valoracion 

#print(evaluacion(4))


print("Programa de Evaluación de Notas de Alumnos")

nota_alumno=int(input("Introduce la nota: "))

def evaluacion(nota):
    valoracion="aprobado"
    if nota <5:
        valoracion="suspenso"
    return valoracion 

#print(evaluacion(int(nota_alumno)))

print(evaluacion(nota_alumno))