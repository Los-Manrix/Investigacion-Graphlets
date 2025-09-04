import os

# Carpeta y archivo a procesar
carpeta = r"C:\Users\benja\Desktop\ManrixPack\ConversionDeMatrices\networks"
archivo_txt = "elec.txt"
ruta = os.path.join(carpeta, archivo_txt)

# Guardamos cada par con su tipo
# {(a,b): tipo}
pares_tipo = {}

# Para mantener el orden de aparición
orden = []

with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
    # Ignoramos la primera línea con la cantidad de pares
    f.readline()
    
    for line in f:
        nums = line.strip().split("\t")
        if len(nums) != 2:
            continue  # Saltar si no tiene dos números
        a, b = map(int, nums)
        par = (a, b)
        par_inv = (b, a)
        
        if par not in pares_tipo and par_inv not in pares_tipo:
            # Par nuevo
            pares_tipo[par] = 1
            orden.append(par)
        elif par in pares_tipo:
            # Ya apareció tal cual antes
            orden.append(par)
        elif par_inv in pares_tipo:
            # Aparece invertido
            # Si el original era tipo 1, ambos pasan a tipo 3
            if pares_tipo[par_inv] == 1:
                pares_tipo[par_inv] = 3
                pares_tipo[par] = 3
            else:
                # Si el original no era tipo 1, el nuevo es tipo 2
                pares_tipo[par] = 2
            orden.append(par)

# Imprimir los pares con su tipo
for p in orden:
    print(p[0], p[1], pares_tipo[p])
