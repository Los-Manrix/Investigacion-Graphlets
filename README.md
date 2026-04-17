# ConversionDeMatrices
Conversión De Matrices para Bio-Informaticos especificando los arcos que unen los nodos mediante un tipo, de esa forma se puede trabajar con grafos no dirigidos para mayor eficiencia.

# Ejecucion
Para ejecutar el codigo es necesario descargar el proyecto y asegurarse de tener python instalado.

Con eso en mente se tiene que que correr el siguiente codigo:

Para linux:

```bash
python3 app.py
```

Para Windows:

```bash
python app.py
```

Esto retornara multiples archivos en diferentes directorios, estos son el indice y una matriz standard con su respectivo formato nuevo que buscamos implementar. Estos se encuentran en los siguientes directorios.

Indices:
```bash
index/indice...txt
```

Matriz standard:
```bash
networks/standards/matrix...txt
```

Matriz nueva
```bash
outs/matrix.._procesada.txt
```

Para tener mas detalles del porque de cada archivo revisar la seccion de 'Utilidad de cada archivo'

# Utilidad de cada archivo creado

El codigo al ejecutarse genera 3 archivos principales, el indice, las matrices standard y las matrices procesadas.

### Indice:

El indice es un archivo en donde se registran los multiples nodos que hay en el archivo tsv original y se les asigna un numero que sirve a modo de indice, para tener una representacion mas sencilla en el grafo final.

El archivo sigue un formato de separcion por tab, en la primera columna se puede ver el indice asignado al nodo, mientras que en la segunda columna se encuentra el nodo extraido del archivo original.

#### Observacion:

Al generarce el indice siempre cambia el orden y la asignacion, al no seguir ningun orden puede que los grafos cambien de una ejecucion de archivo a otra.

### Matriz standard:

La matriz standard sigue un formato de separacion por tabs, en la columna de la izquierda se puede ver el nodo de inicio, mietras que en la columna de la derecha se encuentra el nodo de llegada, ademas, al principio, se agrega el numero de nodos y el numero de arcos, respectivamente.

La matriz standard es un formato que unicamente sirve como punto intermedio entre la matriz procesada y el archivo tsv original, sirve como registro y le sirve al script para generar la matriz nueva.

### Matriz procesada:

La matriz procesada es aquella en la que se plantea el nuevo formato de tres columnas, sigue un fromato de separacion por tabs, en la primera y segunda columna se encuentran los indices de los nodos que estan conectados, mientras que en la tercera columna se encuentra el tipo de coneccion entre ambos. Ademas, al principio del archivo se encuetra el numero de nodos, el numero de arcos originales, el numero de arcos nuevos y el numero de cada tipo de coneccion.
