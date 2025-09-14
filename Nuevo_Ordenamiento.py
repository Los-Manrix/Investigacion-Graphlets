def procesar_pares(nombre_archivo, salida_txt):
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

    # Escribir resultados en archivo de salida
    with open(salida_txt, "w") as f_out:
        for par in lista1:
            a, b = par
            f_out.write(f"{a}\t{b}\t1\n")
            f_out.write(f"{b}\t{a}\t2\n")

        for par in lista2:
            a, b = par
            f_out.write(f"{a}\t{b}\t3\n")
            f_out.write(f"{b}\t{a}\t3\n")


# Rutas de entrada y salida
entrada = r"C:\Users\benja\Desktop\ManrixPack\ConversionDeMatrices\networks\manrix.txt"
salida = r"C:\Users\benja\Desktop\ManrixPack\ConversionDeMatrices\networks\resultado.txt"

procesar_pares(entrada, salida)
