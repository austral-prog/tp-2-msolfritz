def change():
    gasto: 23.75
    Dinero_recibido: 100
    
    Pesos: 76
    Centavos: 25

    gasto = float ("23.75\n")
    Dinero_recibido = float ("100\n")
    vuelto = Dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos)*100))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(int(Dinero_recibido))

    print (" \nVuelto\n")
    print (f"Pesos: \n{pesos}")
    print (f"Centavos: \n{centavos}")
