import os

lista1 = []  # Pares que aparecen solo una vez (tipo 1 y su inverso tipo 2)
lista2 = []  # Pares que aparecen dos veces o más (tipo 3)
aristas = 0  # Contador de todas las aristas leídas
num_nodos = 0  # Número de nodos declarado en el archivo
conteo_tipos = {1: 0, 2: 0, 3: 0}  # Contador de cada tipo de conexión


def procesar_pares(nombre_archivo: str) -> None:
    """
    Procesa un archivo con pares de nodos y genera un archivo de salida que incluye:
    - Resumen: número de nodos, aristas y cantidad de cada tipo de conexión.
    - Listado de pares de nodos con su tipo (1, 2 o 3) según cómo aparezcan.
    """
    global lista1
    global lista2
    global aristas
    global num_nodos
    global num_nodos
    global conteo_tipos

    # Generar nombre del archivo de salida agregando "_procesado" al nombre original

    # Abrir archivo original para lectura
    with open(nombre_archivo, "r") as f:
        primera = f.readline().strip()  # Leer primera línea: número de nodos
        if primera.isdigit():
            num_nodos = int(primera)
        else:
            raise ValueError("La primera línea no es un número válido de nodos.")

        # Leer el resto del archivo línea por línea para procesar las aristas
        for linea in f:
            partes = linea.strip().split()
            if len(partes) != 2:  # Ignorar líneas que no tengan exactamente 2 números
                continue

            a, b = map(int, partes)  # Convertir los nodos a enteros
            aristas += 1  # Contar la arista leída

            par = (a, b)
            par_inv = (b, a)  # Versión invertida del par

            # Clasificar el par según cuántas veces aparece
            if par in lista1 or par_inv in lista1:
                # Si ya estaba en lista1, pasa a lista2 (tipo 3)
                lista1.remove(par if par in lista1 else par_inv)
                lista2.append(par)
            elif par not in lista2 and par_inv not in lista2:
                # Si no está en ninguna lista, agregar a lista1 (tipo 1/2)
                lista1.append(par)

    # Contar cuántos pares hay de cada tipo antes de escribir
    for _ in lista1:
        conteo_tipos[1] += 1  # Tipo 1: par original
        conteo_tipos[2] += 1  # Tipo 2: par invertido
    for _ in lista2:
        conteo_tipos[3] += 2  # Tipo 3: ambos sentidos del par
    return


def escritura(salida: str) -> None:
    global lista1
    global lista2
    global aristas
    global num_nodos
    global num_nodos
    global conteo_tipos

    salida_txt = f"{salida}_procesado.txt"

    with open(salida_txt, "w") as f_out:
        # Resumen al inicio del archivo
        f_out.write(f"Nodos: {num_nodos}\n")
        f_out.write(f"Aristas: {aristas}\n")
        f_out.write(f"Tipo 1: {conteo_tipos[1]}\n")
        f_out.write(f"Tipo 2: {conteo_tipos[2]}\n")
        f_out.write(f"Tipo 3: {conteo_tipos[3]}\n\n")

        # Escribir pares tipo 1 y 2
        for a, b in lista1:
            f_out.write(f"{a}\t{b}\t1\n")  # Tipo 1
            f_out.write(f"{b}\t{a}\t2\n")  # Tipo 2 (invertido)

        # Escribir pares tipo 3
        for a, b in lista2:
            f_out.write(f"{a}\t{b}\t3\n")
            f_out.write(f"{b}\t{a}\t3\n")  # Ambos sentidos
    return


def run() -> None:
    ruta = "./networks/standards"
    counter = 0
    for file in os.listdir(ruta):
        ruta_comp = os.path.join(ruta, file)
        if os.path.isfile(ruta_comp):
            procesar_pares(ruta_comp)
            escritura(f"./outs/matrix{counter}")
            counter =+ 1
    return
