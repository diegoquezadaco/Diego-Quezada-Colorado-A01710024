edades=[]
nombres=[]
telefonos=[]
contactos=[edades,nombres,telefonos]
def operaciones_edades():
    promedio=str(input("Quiere conocer el promedio de edad de sus contactos?: "))
    if promedio=="si":
        suma_edad=sum(contactos[edades])
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
    tel=False
    while tel==False:
        telefono=input("Inserte el número telefónico de su contacto, recuerde que debe ser de 10 digitos: ")
        numnum= telefono.count('')
        numnum=numnum-1
        if numnum!=10 :
            print("Este número de telefono no es válido, por favor intentalo denuevo y digita un número correcto")
        else:
            telefonos.append(telefono)
            tel=True
            pass
    edad=int(input("Inserte la edad de su contacto: "))
    edades.append(edad)
    print("el contacto fue guardado exitosamente")
def buscar_contacto():
    global nom_conuser
    nom_conuser=input("Inserte el nombre de su contacto: ")
    ind=encontrar_ind(nom_conuser)
    if ind!=-1:
        print("Nombre: "+str(nombres[ind])+ "")
        print("Edad: "+str(edades[ind])+ "")
        print("Teléfono: "+str(telefonos[ind])+ "")
    
def eliminar_contacto():
    nom_conuser=input("Inserte el nombre del contacto: ")
    if nom_conuser in nombres:
        pregunta=input("¿Esta seguro que desea eliminar este contacto? ")
        if pregunta=="si":
            ind=nombres.index(nom_conuser)
            nombres.pop(ind)
            telefonos.pop(ind)
            edades.pop(ind)
def editar_contacto():
    nom_conuser= input("Inserte el nombre del contacto que desea editar: ")
    ind=encontrar_ind(nom_conuser)
    if ind!=-1:
        nombres[ind]=input("Inserte el nuevo nombre: ")
        edades[ind]=input("Inserte la nueva edad: ")
        telefonos[ind]=input("Inserte el nuevo número de teléfono: ")
    else:
        preg=input("El contacto no existe. ¿Desea agregar uno nuevo? (si/no) ") == "si"
        if preg:
            crear_contacto()
        else: 
            print("Esta bien")
def ver_contactos():
    print("   _____            _             _            \n  / ____|          | |           | |           \n | |     ___  _ __ | |_ __ _  ___| |_ ___  ___ \n | |    / _ \| '_ \| __/ _` |/ __| __/ _ \/ __|\n | |___| (_) | | | | || (_| | (__| || (_) \__ \ \n  \_____\___/|_| |_|\__\__,_|\___|\__\___/|___/ \n")
    x=len(nombres)
    for i in range(x):
        print("Nombre: "+(nombres[i])+ "")
        print("Número de teléfono: "+str(telefonos[i])+ "")
        print("Edad: "+str(edades[i])+ " años")
    operaciones_edades()
def encontrar_ind(n):
    if n in nombres:
        return nombres.index(n)
    return -1
def menu_app():
    opcion=0
    while opcion!=6:
        print("  __  __              __  \n |  \/  |            /_/  \n | \  / | ___ _ __  _   _ \n | |\/| |/ _ \ '_ \| | | |\n | |  | |  __/ | | | |_| |\n |_|  |_|\___|_| |_|\__,_|\n")
        opcion=int(input("\t1. Crear contacto \n\t2. Editar contacto \n\t3. Buscar contacto \n\t4. Eliminar contacto \n\t5. Ver contacto \n\t6. Salir \n\n"))
        if opcion==1:
            bol=bool
            agregar=input("Desea agregar contactos? ")
            if agregar=="si":
                bol=True
            else:
                bol=False
            while bol==True:
                crear_contacto()
                agregar=input("Desea agregar otro contacto? ")
                if agregar=="no":
                    bol=False
        elif opcion==2:
            editar_contacto()
        elif opcion==3:
            buscar_contacto()
        elif opcion==4:
            eliminar_contacto()
        elif opcion==5:
            ver_contactos()
        elif opcion>=7:
            print("Opción inválida, vuelva a intentarlo")
    print("Gracias por utilizar este programa :)")

menu_app()