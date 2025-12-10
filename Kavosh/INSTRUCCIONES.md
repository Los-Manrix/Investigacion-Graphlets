# Cómo ejecutar Kavosh con tu propia red

El archivo de red que quieres procesar **no se define dentro del código fuente**, sino que se pasa como un argumento al ejecutar el programa en la terminal.

## Sintaxis del comando

Para ejecutar el programa, utiliza la siguiente estructura en la terminal:

```bash
./Kavosh -i <ruta_al_archivo_de_red> -s <tamaño_del_motivo> [opciones]
```

### Parámetros principales:

*   `-i` o `--input`: **(Obligatorio)** La ruta al archivo que contiene tu red.
*   `-s` o `--size`: **(Obligatorio)** El tamaño del motivo (subgrafo) que quieres buscar (ej. 3, 4, etc.).
*   `-r` o `--random`: (Opcional) Número de grafos aleatorios para generar y comparar (para calcular la significancia estadística). Por defecto es 0.
*   `-o` o `--output`: (Opcional) Carpeta donde se guardarán los resultados. Por defecto es `result`.

## Ejemplos

1.  **Ejemplo básico:**
    Procesar la red `networks/yeast` buscando motivos de tamaño 3:
    ```bash
    ./Kavosh -i networks/yeast -s 3
    ```

2.  **Con grafos aleatorios:**
    Procesar tu propio archivo `mi_red.txt`, buscando motivos de tamaño 4 y comparando con 100 grafos aleatorios:
    ```bash
    ./Kavosh -i mi_red.txt -s 4 -r 100
    ```

3.  **Guardando en otra carpeta:**
    Guardar los resultados en la carpeta `mis_resultados`:
    ```bash
    mkdir -p mis_resultados
    ./Kavosh -i networks/social -s 3 -o mis_resultados
    ```

## Formato del archivo de entrada

Para que el programa funcione con tu propia red, el archivo debe seguir este formato (lista de aristas):

```text
<número_total_de_nodos>
<nodo_origen> <nodo_destino>
<nodo_origen> <nodo_destino>
...
```

**Ejemplo de archivo (`mi_red.txt`):**
```text
4
1 2
2 3
3 4
4 1
```
*   La primera línea es el número total de nodos.
*   Las siguientes líneas son las conexiones (aristas) entre nodos.
