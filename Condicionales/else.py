#print("Verificación de Acceso")

#edad_usuario=int(input("Introduce tu edad: "))

#if edad_usuario < 18:
#    print("No puedes entrar")
#elif edad_usuario >100:
#   print("Edad Incorrecta")
#else:
#    print("Puedes pasar")
#print("El programa ha finalizado")


print("Verificación de Acceso")

nota_alumno=int(input("Introduce tu nota: "))

if nota_alumno <5:
    print("Insuficiente")
elif nota_alumno <6:
    print("Suficiente")
elif nota_alumno <7:
    print("Bien")
elif nota_alumno <9:
    print("Notable")
else:
    print("Sobresaliente")