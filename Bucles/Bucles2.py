
#email=False
#miEmail=input("introduce tu email: ")

#for i in miEmail:
#    if(i=="@"):
#        email=True
#if email:
#    print("email es correcto")
#else:
#    print("el email no es correcto")



contador=0
miEmail=input("introduce tu email: ")

for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador==2:
    print("email correcto")
else:
    print("email incorrecto)


for a in range(5):
    print("hola")
    print(a)



for i in range(5):
    print(f"valor de la variable {i}")