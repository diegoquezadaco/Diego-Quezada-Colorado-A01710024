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

importar libreria

CARPETA DE CONTACTOS= 'Contactos.txt'
#le damos un valor inicial a nuestras variables
definir (nombre,numero,categoria):
        nombre=''
        numero=0
        residencia=''
        foto=(archivo .png)
#funcion principal
definir listcontacts():
    pregunta=Verdad
    opcion=input('Selecciona una de las opciones disponibles')
    print('1. Agregar contacto
            2. Editar contacto
            3. Ver contactos
            4. Buscar contacto
            5. Eliminar contacto)
    definir mostmenu():
        mientras pregunta=Verdad
            opcion=input('Seleccione una de las siguientes opciones')
                if opcion=='1':
                    agregar_contacto()
                    preguntar=Falso
                elif opcion=='2':
                    editar_contacto()
                    preguntar=Falso
                elif opcion=='3':
                    ver_contacto()
                    preguntar=Falso
                elif opcion=='4':
                    buscar_contacto()
                    preguntar=Falso
                elif opcion=='5':
                    eliminarar_contacto()
                    preguntar=Falso
                else: 
                    print('Opción no válida, intentelo de nuevo')
    mostmenu():
    definir agregar_contacto():
        print('Escribe los datos que tendra tu nuevo contacto')
        nombre_contacto=input('Nombre:')
        #Revisar si el archivo ya existe antes de crearlo
        existe=buscar.libreria(CARPETA +nombre_contacto+ )
        if not existe:
            with editar.libreria(CARPETA +nombre_contacto+ ):        
                #Llenamos el resto de los campos
                numero_contacto=input('Número telefonico: ')
                categoria_contacto=input('Categoria del contacto: ')

                enviaratxt.libreria():

                #Decirle al usuario que se guardo correctamente
                print('Contacto Guardado Correctamente :)')
        else:
            print('Este contacto ya existe en tu lista')
#despues de todo, volvemos a llamar a la función, para que pueda seguir guardando contactos
listcontacts()
#nota: se que este código esta incompleto, pero como necesitamos el uso de una librería, hay muchas funciones
de la lista de contactos que no pude definir porque no se como interactuarían con las otras funciones, así que
trate de describir lo mejor posible mi idea, usando las funciones que conozco.
"""