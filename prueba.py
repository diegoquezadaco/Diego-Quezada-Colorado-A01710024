operar= False
pregunta=str(input("Quiere hacer las operaciones? "))
if pregunta=="si":
    operar=True
    while operar==True:
        a=float(input("Proporcioneme el primer valor: "))
        b=float(input("Proporcioneme el segundo valor: "))
        c=float(input("Proporcioneme el tercer valor: "))
        res1=a/b
        res2=a%b
        res3=a/b-c
        res4=a/(b-c)
        print(f"el resultado de la operación 1 es: {res1}")
        print(f"el resultado de la operación 2 es: {res2}")
        print(f"el resultado de la operación 3 es: {res3}")
        print(f"el resultado de la operación 4 es: {res4}")
        pregunta=str(input("Quiere hacer más operaciones?: "))
        if pregunta=="si":
            operar=True
        else:
            operar=False
            print("Gracias por utilizar este operador")
else:
    print("Gracias por utilizar este operador :)")

