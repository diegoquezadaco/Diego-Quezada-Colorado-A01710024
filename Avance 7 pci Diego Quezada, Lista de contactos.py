edades=[]
nombres=[]
telefonos=[]
contactos=[edades,nombres,telefonos]
EDADES=0
NOMBRES=1
TELEFONOS=2
def operaciones_edades() :
    promedio=str(input("Quiere conocer el promedio de edad de sus contactos?: "))
    if promedio=="si":
        suma_edad=sum(contactos[EDADES])
        num_edad=len(contactos[EDADES])
        resprom=suma_edad/num_edad
        print("El promedio de las edades de sus contactos es de " + str(resprom) +" años.")
    else:
        print("Esta bien :)")
    maxmin=input("¿Desea conocer su la mayor y la menor edad de su lista de contactos? (si/no) ") == "si"
    if maxmin:
        print("La mayor edad de su lista es de " +str(max(contactos[EDADES]))+ " años")
        print("La menor edad de su lista es de " +str(min(contactos[EDADES]))+ " años")
    else:
        print("Esta bien :)")
    repetida=str(input("Quiere conocer su edad más repetida en su lista de contactos?: "))
    if repetida=="si":
        repet=max(set(contactos[EDADES]), key=(contactos[EDADES]).count)
        print("La edad que más se repite en su lista de contactos es "+str(repet)+ " años")
def crear_contacto():
    nom=True
    while nom==True:
        nom_conuser=input("Inserte el nombre de su nuevo contacto: ")
        ind=encontrar_ind(nom_conuser)
        if ind==-1:
            print("Puede agregar el contacto")
            contactos[NOMBRES].append(nom_conuser)
            tel=False
            while tel==False:
                telefono=input("Inserte el número telefónico de su contacto, recuerde que debe ser de 10 digitos: ")
                numnum= telefono.count('')
                numnum=numnum-1
                if numnum!=10 :
                    print("Este número de telefono no es válido, por favor intentalo denuevo y digita un número correcto")
                else:
                    (contactos[TELEFONOS]).append(telefono)
                    tel=True
            edad=int(input("Inserte la edad de su contacto: "))
            (contactos[EDADES]).append(edad)
            nom=False
        else:
            print("Este contacto ya existe, por favor intentelo de nuevo")
    print("el contacto fue guardado exitosamente")
def buscar_contacto():
    global nom_conuser
    nom_conuser=input("Inserte el nombre de su contacto: ")
    ind=encontrar_ind(nom_conuser)
    if ind!=-1:
        print("Nombre: "+str(contactos[NOMBRES][ind])+ "")
        print("Edad: "+str(contactos[EDADES][ind])+ " años")
        print("Teléfono: "+str(contactos[TELEFONOS][ind])+ "")
def eliminar_contacto():
    nom_conuser=input("Inserte el nombre del contacto: ")
    if nom_conuser in (contactos[NOMBRES]):
        pregunta=input("¿Esta seguro que desea eliminar este contacto? ")
        if pregunta=="si":
            ind=(contactos[NOMBRES]).index(nom_conuser)
            contactos[NOMBRES].pop(ind)
            contactos[TELEFONOS].pop(ind)
            contactos[EDADES].pop(ind)
def editar_contacto():
    nom_conuser= input("Inserte el nombre del contacto que desea editar: ")
    ind=encontrar_ind(nom_conuser)
    if ind!=-1:
        contactos[NOMBRES][ind]=input("Inserte el nuevo nombre: ")
        contactos[TELEFONOS][ind]=input("Inserte el nuevo número de teléfono: ")
    else:
        preg=input("El contacto no existe. ¿Desea agregar uno nuevo? (si/no) ") == "si"
        if preg:
            crear_contacto()
        else: 
            print("Esta bien")
def ver_contactos():
    with open("titulocontactos.txt", encoding="utf-8") as diccionario:
        palabra=diccionario.read()
        print(palabra)
    x=len(nombres)
    for i in range(x):
        print("Nombre: "+(contactos[NOMBRES][i])+ "")
        print("Número de teléfono: "+str(contactos[TELEFONOS][i])+ "")
        print("Edad: "+str(contactos[EDADES][i])+ " años")
        print("------------------------------------------")
    operaciones_edades()
def encontrar_ind(n):
    if n in nombres:
        return contactos[NOMBRES].index(n)
    return -1
def menu_app():
    opcion=0
    while opcion!=6:
        with open("titulomenu.txt", encoding="utf-8") as diccionario:
            palabra=diccionario.read()
            print(palabra)
        opcion=int(input("\t1. Crear contacto \n\t2. Editar contacto \n\t3. Buscar contacto \n\t4. Eliminar contacto \n\t5. Ver contactos \n\t6. Salir \n\n"))
        if opcion==1:
            bol=True
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