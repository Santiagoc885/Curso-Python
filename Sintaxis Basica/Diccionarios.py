#Diccionarios: estructura de datos que nos permite almacenar valores de diferentes tipos

#CLAVE UNICA

#diccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
#print(diccionario["Francia"])
#AGREGAR OTRO ELEMENTO AL DICCIONARIO

#diccionario["Italia"]="Roma"

#PARA ELIMINAR UN ELEMENTO

#del diccionario["Reino Unido"]
#print(diccionario)
#tupla a diccionario
#mitupla=["España","Francia","Reino Unido","Alemania"]
#midiccionario={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}

#print(midiccionario["Francia"])

midiccionario={23:"Jordan", "Nombre":"Michael","Equipo":"Lakers","Anillos":{"Temporadas":[1991,1992,1993]}}
#print(midiccionario["Anillos"])
#MOSTRAR LAS PALABRAS
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))