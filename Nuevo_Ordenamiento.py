ruta = r"C:\Users\xxx\OneDrive\Escritorio\xxx\ConversionDeMatrices\networks\social.txt"

pares_tipo1 = set()
pares_tipo2 = set()

lineas_salida = []

with open(ruta, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        nums = line.strip().split()
        if len(nums) != 2:
            continue
        a, b = int(nums[0]), int(nums[1])
        par = (a, b)
        par_inv = (b, a)

        if par not in pares_tipo1 and par_inv not in pares_tipo1:
            # Par nuevo, tipo 1
            lineas_salida.append((a, b, 1))
            pares_tipo1.add(par)
        elif par_inv in pares_tipo1 and par not in pares_tipo2:
            # Aparece inverso, tipo 2
            lineas_salida.append((a, b, 2))
            pares_tipo2.add(par)
            # Añadimos tipo 3 solo para este par tipo 2
            lineas_salida.append((a, b, 3))
        else:
            # Si par ya fue tipo 1 o 2, ignorar repetidos
            pass

for a, b, t in lineas_salida:
    print(a, b, t)

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
