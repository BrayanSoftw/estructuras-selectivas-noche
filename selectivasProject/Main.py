# ESTRUCTURA SIMPLE
a=33
b=200

if b > a:
    print(b,"es mayor que",a)

#ESTRUCTURA DOBLE
if a>b:
    print(b,"es mayor que",a)
else:
    print(b,"No es mayor que",a)

#ESTRUCTURA MULTIPLE "elif SINO SI" REMPLAZO DE CASE EN JAVA
a=200
b=207
if a>b:
    print(a,"es mayor que",b)
elif a<b:
    print(a,"es menor que",b)
else:
    print(a,"es igual que",b)
#ESTRUCTURA ENLAZADA
x=28

if x> 10:
    print("por encima de diez,")
    if x >20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")
#PARAMETRO END
print("Estudiar los sabados", end='')
print("es genial")
#PARAMETRO SEP
print("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")#Quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#Agrega una coma

print("Daniela","Luis","Carlos","Camila",sep="_",end="_Curso_python")#Implementacion end y sep
