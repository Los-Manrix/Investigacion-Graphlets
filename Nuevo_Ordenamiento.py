def procesar_pares(nombre_archivo):
    lista1 = []  # pares que aparecen una vez
    lista2 = []  # pares que aparecen dos veces

    with open(nombre_archivo, "r") as f:
        for linea in f:
            # limpiar la línea
            partes = linea.strip().split()
            if len(partes) != 2:
                continue  # saltar si no tiene exactamente 2 números

            a, b = map(int, partes)
            par = (a, b)
            par_inv = (b, a)

            # Revisar si par o invertido está en lista1
            if par in lista1 or par_inv in lista1:
                if par in lista1:
                    lista1.remove(par)
                else:
                    lista1.remove(par_inv)
                lista2.append(par)
            elif par not in lista2 and par_inv not in lista2:
                lista1.append(par)

    # Imprimir resultados
    for par in lista1:
        a, b = par
        print(a, b, 1)
        print(b, a, 2)

    for par in lista2:
        a, b = par
        print(a, b, 3)
        print(b, a, 3)


ruta = r"C:\Users\benja\Desktop\ManrixPack\ConversionDeMatrices\networks\manrix.txt"
procesar_pares(ruta)