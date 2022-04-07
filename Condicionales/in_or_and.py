# print("Programa de becas ano 2017")
# distancia_escuela=int(input("Introduce la distancia a la escuela"))
# print(distancia_escuela)

# nuumero_hermanos=int(input("introduce el n° de hermano"))
# print(nuumero_hermanos)


# salario_familiar=int(input("introduce el salario anual"))
# print(salario_familiar)

# if distancia_escuela>40 and nuumero_hermanos>2 or salario_familiar<=20000:
#     print("tienes derecho a beca")
# else:
#    print("no tienes derecho a beca")

print("Asignaturas año 2022")
print("Informatica - pruebas de software- usabilidad")

opcion=input("escribe la asignatura escogida")
asignatura=opcion.lower()

if asignatura in ("informatica","pruebas de software", "usabilidad"):
    print("Asignatura escogida" + asignatura)
else:
    print("la asignatura no esta")