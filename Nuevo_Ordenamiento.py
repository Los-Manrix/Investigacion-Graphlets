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

"""
===================================================================================
EXPLICACIÓN DEL ALGORITMO:

Este código procesa una lista de pares dirigidos (a,b) que representan conexiones en un grafo.

- Tipo 1: Cuando un par (a,b) aparece por primera vez y su inverso (b,a) no ha aparecido aún.
- Tipo 2: Cuando aparece el par inverso (b,a) de un par que ya era tipo 1.
- Tipo 3: Se agrega una línea adicional para representar bidireccionalidad cuando
  un par tipo 2 aparece, mostrando que existe una conexión en ambos sentidos.

Pasos:

1. Se almacenan los pares tipo 1 en un conjunto.
2. Si aparece el inverso de un par tipo 1, ese nuevo par se clasifica como tipo 2.
3. Además, se añade una línea tipo 3 para mostrar bidireccionalidad, pero no se elimina
   la información de tipo 1 o 2.
4. Se ignoran pares repetidos para evitar impresiones duplicadas.

Ejemplo práctico:

Dado un archivo con pares:
1 2
2 1
1 3
3 1
2 4
4 2

El resultado es:
1 2 1  (aparece primero, tipo 1)
2 1 2  (inverso, tipo 2)
2 1 3  (bidireccionalidad)
1 3 1  (nuevo par, tipo 1)
3 1 2  (inverso, tipo 2)
3 1 3  (bidireccionalidad)
2 4 1  (nuevo par, tipo 1)
4 2 2  (inverso, tipo 2)
4 2 3  (bidireccionalidad)

Esto permite detectar conexiones unidireccionales (tipos 1 y 2) y bidireccionales (tipo 3),
lo cual es importante para analizar la estructura del grafo y sus patrones de conexión.

===================================================================================
"""
