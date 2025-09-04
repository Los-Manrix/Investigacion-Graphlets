import os

carpeta = r"C:\Users\benja\Desktop\ManrixPack\ConversionDeMatrices\networks"
archivo_txt = "elec.txt"
ruta = os.path.join(carpeta, archivo_txt)


pares_tipo = {}

orden = []

with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
    first_line = f.readline()  # Ignoramos la primera línea
    for line in f:
        nums = line.strip().split("\t")
        if len(nums) != 2:
            continue
        a, b = map(int, nums)
        par = (a, b)
        par_invertido = (b, a)

        if par not in pares_tipo and par_invertido not in pares_tipo:
            # Par nuevo → tipo 1
            pares_tipo[par] = 1
            orden.append(par)
        elif par in pares_tipo:
            # Ya existía en el mismo orden → sigue tipo 1
            orden.append(par)
        else:
            # Es invertido → tipo 3
            # Actualizamos el tipo del original a 3 también
            pares_tipo[par_invertido] = 3
            pares_tipo[par] = 3
            orden.append(par)


for p in orden:
    print(p[0], p[1], pares_tipo[p])

        
