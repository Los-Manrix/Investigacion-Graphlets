import os

def procesar_pares(nombre_archivo: str):
    """
    Lee un archivo de matriz y clasifica los pares (a,b) según su aparición:
    - Tipo 1/2: par único y su inverso
    - Tipo 3: pares bidireccionales (aparecen ambos sentidos)
    Retorna estadísticas y listas de pares.
    """
    pares = set()
    bidireccionales = set()
    aristas = 0

    with open(nombre_archivo, "r") as f:
        primera = f.readline().strip()
        if not primera.isdigit():
            raise ValueError("La primera línea no es un número válido de nodos.")
        num_nodos = int(primera)

        for linea in f:
            partes = linea.strip().split()
            if len(partes) != 2:
                continue

            a, b = map(int, partes)
            aristas += 1

            if (b, a) in pares:
                bidireccionales.add((a, b))
                bidireccionales.add((b, a))
            pares.add((a, b))

    # Tipos 1/2 = los pares que no son bidireccionales
    unidireccionales = [p for p in pares if p not in bidireccionales]

    conteo_tipos = {
        1: len(unidireccionales),
        2: len(unidireccionales),
        3: len(bidireccionales) // 2  # cada par cuenta doble
    }

    return num_nodos, aristas, unidireccionales, bidireccionales, conteo_tipos


def escritura(salida: str, num_nodos, aristas, unidireccionales, bidireccionales, conteo_tipos):
    salida_txt = f"{salida}_procesado.txt"
    buffer = []

    buffer.append(f"Nodos: {num_nodos}\n")
    buffer.append(f"Aristas: {aristas}\n")
    buffer.append(f"Tipo 1: {conteo_tipos[1]}\n")
    buffer.append(f"Tipo 2: {conteo_tipos[2]}\n")
    buffer.append(f"Tipo 3: {conteo_tipos[3]}\n\n")

    # Unidireccionales (1 y 2)
    for a, b in unidireccionales:
        buffer.append(f"{a}\t{b}\t1\n")
        buffer.append(f"{b}\t{a}\t2\n")

    # Bidireccionales (3)
    for a, b in bidireccionales:
        buffer.append(f"{a}\t{b}\t3\n")

    with open(salida_txt, "w") as f_out:
        f_out.writelines(buffer)


def run():
    ruta = "./networks/standards"
    os.makedirs("./outs", exist_ok=True)
    counter = 0

    for file in os.listdir(ruta):
        ruta_comp = os.path.join(ruta, file)
        if os.path.isfile(ruta_comp):
            num_nodos, aristas, uni, bi, conteo = procesar_pares(ruta_comp)

            nombre_base = os.path.splitext(os.path.basename(file))[0]
            salida = f"./outs/{nombre_base}"

            escritura(salida, num_nodos, aristas, uni, bi, conteo)
            counter += 1
        print(ruta_comp)


if __name__ == "__main__":
    run()
