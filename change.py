def cambio():
    Gasto = 23.75
    Dinero = 100

    Vuelto = Dinero - Gasto

    Pesos = int(Vuelto)
    Centavos = int((Vuelto - Pesos)*100)

    print("\nVuelto\n")
    print(f"Pesos:\n{Pesos}")
    print(f"Centavos:\n{Centavos}")
    
