# Diego Quezada Colorado A01710024 README PCI Python

"""
Este algoritmo tiene la función de crear una lista de contactos y guardarlos en un archivo .txt , definiendo 
clases y atributos previamente para esto, previamente tenemos que definir el nombre de nuesta carpeta de 
contactos. Pero antes de todo, debemos hacer uso de una librería de python que nos permita administrar 
archivos y nos de funciones extra que nos ayuden a crear y eliminar dichos contactos. Posteriormente,
podemos definir dichas variables y y también el menú que nos permita desplazarnos a lo largo de la libreta
de contactos sin necesidad de abrir nuestra pequeña "base de datos" y que todo sea una experiencia más cómoda
para el usuario en cuestión, dicha función se realizaría a ravés de opciones, que fácilmente podríamos definir
con valores numéricos, en un menú que se le presente al usuario previamente.

Asimismo, debemos añadir funciones que hagan un poco más realista esta libreta de contactos, que nos permitan
editar, guardar, borrar, buscar y añadir nuevos contactos. Todo esto sería a través de funciones proporcionadas
por la librería en cuestión.

Por tanto, para realizar dicho programa podríamos hacer lo siguiente:

#Paso 1 definir algoritmos
Crear contacto
Editar contacto
Buscar contacto
Eliminar contacto
Ver contactos
Salir
#Definir algoritmo principal
Menu
Nombre, numero y edad
promedio de edad de tus contactos
la edad que más repita
la menor y la mayor (el contacto)
#Definir valores iniciales
opcion=0
1. Mostrar el menú
2. preguntar al usuario la opcion (opcion=entrada)
3. mientras la opción sea diferente de 6
    3.1. Si la opcion=1
        3.1.1. Ejecutar "crear contacto"
    3.2. Si la opcion=2
        3.2.1. Ejecutar "editar contacto"
    3.3. Si la opcion=3
        3.3.1. Ejecutar "buscar contacto"
    3.4. Si la opcion=4
        3.4.1. Ejecutar "eliminar contacto"
    3.5. Si la opcion=5
        3.5. Ejecutar "ver contactos"
    3.6. Si la opcion no es ninguna de las anteriores
        3.6.1. mandar un mensaje de error
    3.7. preguntar si quiere seguir utilizando la app
        3.7.1. si dice que si
            3.7.1.1. Mostrar el menú y volver a preguntar la opción 
        3.7.2. si no
            3.7.2.1. Opcion=6
4. Mostrar despedida
diccionarios tiene un indice alfanumérico
#FIN

#Definir las funciones de los algoritmos
Crear contacto:
    1. Pedir al usuario el nombre del nuevo contacto
        1.1. llamar a la función "buscar contacto" y checar que no exista un contacto del mismo nombre
        1.2 si existe
            1.2.1. Mostrar un mensaje de error
        1.3 si no existe
            1.3.1. Pedir número de telefono
            1.3.2. Pedir edad del contacto
            1.3.3. Guardar los datos en el diccionario
            1.3.4. Mostrar mensaje de éxito
Editar contacto: 
    1. Pedir al usuario el nombre
    2. Llamar a la función "buscar contacto"
    3. Solicitar la búsqueda de la cadena proporcionada por el usuario
    4. si existe
        4.1. llamar la función de "eliminar contacto"
        4.2 llamar la función de "crear contacto"
            4.2.1. solicitar al usuario los datos otra vez (nombre, teléfono y edad)
            4.2.2. guardar el nuevo contacto
            4.2.3. Mostrar un mensaje de éxito
    5. si no existe
        5.1 Mostrar un mensaje de error
Buscar contactos:
    1.Pedir al usuario el nombre
    2. Buscar la cadena proporcionada por el usuario en el diccionario
    3. Si existe
        3.1. Mostrar nombre, teléfono y edad del contacto solicitado
    4. Si no existe
        4.1 Mostrar un mensaje de error
Eliminar contacto:
    1. Pedir al usuario el nombre
    2. Llamar a la función "buscar contacto"
    3. Si existe
        3.2. Borrar elemento del diccionario 
        3.3. Mostrar mensaje de éxito
    4. Si no existe
        4.1 Mostrar un mensaje de error
Ver contactos:
    1. Imprimir "Aquí esta su lista de contactos"
    2. Imprimir todo el diccionario seccionado por nombre, telefono y edad
    3. Preguntar al usuario si quiere saber datos interesantes acerca de la edad de sus contactos
    4. Si dice que si
        4.1 Imprimir "el promedio de edades de sus contactos es {promedio}"
        4.2 Imprimir "La edad que más se repite en sus contactos es {moda}"
        4.3 Imprimir "Su contacto más joven es {menorn}"
        4.4 Imprimir "Su contacto más viejo es {mayorn}"
        4.5 Mostrar un mensaje de éxito
    5. Si dice que no
        5.1 Mostrar un mensaje de éxito.
    
promedio de edad de tus contactos
la edad que más repita
la menor y la mayor (el contacto)
"""


from ast import Global


edades=[]
nombres=[]
telefonos=[]
def operaciones_edades():
    promedio=str(input("Quiere conocer el promedio de edad de sus contactos?: "))
    if promedio=="si":
        suma_edad=sum(edades)
        num_edad=len(edades)
        resprom=suma_edad/num_edad
        print("El promedio de las edades de sus contactos es de " + str(resprom) +" años.")
    else:
        print("Esta bien :)")
    maximo=str(input("¿Quiere conocer la edad máxima y minima de su lista de contactos? "))
    if maximo=="si":
        maxim=max(edades)
        minim=min(edades)
        print("La mayor edad de su lista es de " +str(maxim)+ " años")
        print("La menor edad de su lista es de " +str(minim)+ " años")
    else:
        print("Esta bien :)")
    repetida=str(input("Quiere conocer su edad más repetida en su lista de contactos?: "))
    if repetida=="si":
        repet=max(set(edades), key=edades.count)
        print("La edad que más se repite en su lista de contactos es "+str(repet)+ " años")
def crear_contacto():
    buscar_contacto()
    print("Puede agregar el contacto")
    nombres.append(nom_conuser)
    telefono=input("Inserte el número telefónico de su contacto, recuerde que debe ser de 10 digitos: ")
    numnum= telefono.count('')
    numnum=numnum-1
    if numnum!=10 :
        print("Este número de telefono no es válido, por favor intentalo denuevo y digita y número correcto")
    else:
        telefonos.append(telefono)
        pass
    edad=int(input("Inserte la edad de su contacto: "))
    edades.append(edad)
    print("el contacto fue guardado exitosamente")    
def buscar_contacto():
    global nom_conuser
    nom_conuser=input("Inserte el nombre de su nuevo contacto: ")
    if nom_conuser in nombres:
        print("El nombre ya existe en la lista, por favor intentelo de nuevo")
    else:
        pass
def eliminar_contacto():
    buscar_contacto()
    pregunta=input("¿Esta seguro que desea eliminar este contacto? ")
    if pregunta=="si":
        nombres.pop(nom_conuser)
    else:
        pass
def editar_contacto():
    buscar_contacto()
    print("Puede editar el contacto")
    eliminar_contacto()
    crear_contacto()
    print("El contacto fue guardado exitosamente")
https://onlinegdb.com/6ERrgS7l0

