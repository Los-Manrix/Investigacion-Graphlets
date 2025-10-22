#include <stdio.h>
#include <stdlib.h>

// ============================================================================
// ?? ESTRUCTURAS BASE
// ============================================================================

// Declaración anticipada
typedef struct Nodo Nodo;

// Estructura que representa un arco (una conexión entre nodos)
typedef struct Arco {
    Nodo* destino;          // Nodo al que apunta este arco
    struct Arco* siguiente; // Siguiente arco en la lista de adyacencia
} Arco;

// Nodo del grafo
struct Nodo {
    int id;             // Identificador único del nodo
    int color;          // 0 = blanco, 1 = rojo (para marcar visitados)
    int iter;           // Iteración actual (usado en la búsqueda)
    int tipoConexion;   // Tipo de conexión (según función t)
    Nodo* padre;        // Nodo padre en el recorrido
    Arco* arcos;        // Lista de arcos salientes (adyacentes)
};

// Grafo completo
typedef struct {
    Nodo** listaNodos;  // Arreglo de punteros a nodos
    int totalNodos;     // Cantidad de nodos
} Grafo;

// ============================================================================
// ?? ESTRUCTURA DE COLA (para recorrido BFS o similar)
// ============================================================================

typedef struct NodoCola {
    Nodo* dato;
    struct NodoCola* siguiente;
} NodoCola;

typedef struct {
    NodoCola* frente;
    NodoCola* final;
} Cola;

// Crea una nueva cola vacía
Cola* crearCola() {
    Cola* q = (Cola*)malloc(sizeof(Cola));
    q->frente = NULL;
    q->final = NULL;
    return q;
}

// Verifica si la cola está vacía
int colaVacia(Cola* q) {
    return q->frente == NULL;
}

// Inserta un nodo al final de la cola
void colaInsertar(Cola* q, Nodo* n) {
    NodoCola* nuevo = (NodoCola*)malloc(sizeof(NodoCola));
    nuevo->dato = n;
    nuevo->siguiente = NULL;

    if (q->final == NULL)
        q->frente = nuevo;
    else
        q->final->siguiente = nuevo;

    q->final = nuevo;
}

// Extrae un nodo desde el frente de la cola
Nodo* colaPop(Cola* q) {
    if (colaVacia(q)) return NULL;
    NodoCola* aux = q->frente;
    Nodo* n = aux->dato;
    q->frente = aux->siguiente;
    if (q->frente == NULL)
        q->final = NULL;
    free(aux);
    return n;
}

// ============================================================================
// ?? FUNCIONES AUXILIARES
// ============================================================================

// Cálculo de combinaciones (nCk)
int combinatoria(int n, int k) {
    if (k > n) return 0;
    if (k == 0 || k == n) return 1;
    return combinatoria(n - 1, k - 1) + combinatoria(n - 1, k);
}

// Función simbólica t(a, b)
int tipoRelacion(Nodo* a, Nodo* b) {
    printf("t(%d, %d)\n", a->id, b->id);
    return 1; // Valor simbólico (puedes definir tu propia lógica)
}

// Agregar un arco (una dirección)
void agregarArco(Nodo* origen, Nodo* destino) {
    Arco* nuevo = (Arco*)malloc(sizeof(Arco));
    nuevo->destino = destino;
    nuevo->siguiente = origen->arcos;
    origen->arcos = nuevo;
}

// Agregar arista bidireccional (no dirigido)
void agregarAristaNoDirigida(Nodo* a, Nodo* b) {
    agregarArco(a, b);
    agregarArco(b, a);
}

// ============================================================================
// ?? FUNCIONES PRINCIPALES DE BÚSQUEDA
// ============================================================================

void searchMotifDriver(Grafo* grafo);
void searchMotif(Grafo* grafo, Nodo* nodoInicio, int iter);

// Controlador principal de búsqueda (itera por cada nodo)
void searchMotifDriver(Grafo* grafo) {
    int iteracion = 1;


    for (int i = 0; i < grafo->totalNodos; i++) {
        searchMotif(grafo, grafo->listaNodos[i], iteracion);
        iteracion++;
    }
}

// Búsqueda de motivos a partir de un nodo específico
void searchMotif(Grafo* grafo, Nodo* nodoInicio, int iter) {
    Cola* q = crearCola();
    nodoInicio->padre = NULL;
    nodoInicio->color = 1; // rojo = visitado

    int nTipo1 = 0, nTipo2 = 0, nTipo3 = 0;
	Arco* arco;
    // Recorre los nodos adyacentes al nodo de inicio
    for (arco = nodoInicio->arcos; arco != NULL; arco = arco->siguiente) {
        Nodo* nodoDestino = arco->destino;

        if (nodoDestino->color != 1) {
            nodoDestino->tipoConexion = tipoRelacion(nodoInicio, nodoDestino);

            if (nodoDestino->tipoConexion == 1) nTipo1++;
            if (nodoDestino->tipoConexion == 2) nTipo2++;
            if (nodoDestino->tipoConexion == 3) nTipo3++;

            nodoDestino->padre = nodoInicio;
            colaInsertar(q, nodoDestino);
        }
    }

    // Ejemplo de operaciones combinatorias simbólicas
    printf("s.t(1,0,1) = C(%d,2)\n", nTipo1);
    printf("s.t(2,0,2) = C(%d,2)\n", nTipo2);
    printf("s.t(3,0,3) = C(%d,2)\n", nTipo3);

    printf("s.t(1,0,2) = C(%d,2) - ...\n", nTipo1 + nTipo2);
    printf("s.t(1,0,3) = C(%d,2) - ...\n", nTipo1 + nTipo3);
    printf("s.t(2,0,3) = C(%d,2) - ...\n", nTipo2 + nTipo3);

    // Recorre la cola (BFS)
    while (!colaVacia(q)) {
        Nodo* nodoActual = colaPop(q);
        nodoActual->iter = iter;
		Arco* arco;
        for (arco = nodoActual->arcos; arco != NULL; arco = arco->siguiente) {
            Nodo* nodoDestino = arco->destino;

            if (nodoDestino->color != 1 && nodoDestino->iter != iter) {
                if (nodoDestino->padre == nodoActual->padre) {
                    printf("Caso igual: padre.t(%d,0,%d)-- y ++\n", 
                           nodoActual->tipoConexion, nodoDestino->tipoConexion);
                } else {
                    printf("Caso distinto: padre.t(%d,%d,0)++\n", 
                           nodoActual->tipoConexion, tipoRelacion(nodoActual, nodoDestino));
                }
            }
        }
    }

    free(q);
}

// ============================================================================
// ?? MAIN — Lectura desde archivo
// ============================================================================

int main() {
	int i;
    char nombreArchivo[100];
    printf("Ingrese el nombre del archivo del grafo: ");
    scanf("%s", nombreArchivo);

    FILE* archivo = fopen(nombreArchivo, "r");
    if (!archivo) {
        printf("? No se pudo abrir el archivo '%s'\n", nombreArchivo);
        return 1;
    }

    int numNodos, numAristas;
    fscanf(archivo, "%d %d", &numNodos, &numAristas);

    Grafo grafo;
    grafo.totalNodos = numNodos;
    grafo.listaNodos = (Nodo*)malloc(sizeof(Nodo) * numNodos);

    // Inicializa nodos
    for (i = 0; i < numNodos; i++) {
        grafo.listaNodos[i] = (Nodo*)malloc(sizeof(Nodo));
        grafo.listaNodos[i]->id = i + 1;
        grafo.listaNodos[i]->color = 0;
        grafo.listaNodos[i]->iter = 0;
        grafo.listaNodos[i]->tipoConexion = 0;
        grafo.listaNodos[i]->padre = NULL;
        grafo.listaNodos[i]->arcos = NULL;
    }

    // Lectura de aristas
    for (i = 0; i < numAristas; i++) {
        int origen, destino, tipo;
        fscanf(archivo, "%d %d %d", &origen, &destino, &tipo);
        agregarAristaNoDirigida(grafo.listaNodos[origen - 1], grafo.listaNodos[destino - 1]);
    }

    fclose(archivo);

    // Ejecuta búsqueda de motivos
    searchMotifDriver(&grafo);

    // Liberar memoria
    for (i = 0; i < grafo.totalNodos; i++) {
        Arco* arco = grafo.listaNodos[i]->arcos;
        while (arco != NULL) {
            Arco* temp = arco;
            arco = arco->siguiente;
            free(temp);
        }
        free(grafo.listaNodos[i]);
    }
    free(grafo.listaNodos);

    return 0;
}