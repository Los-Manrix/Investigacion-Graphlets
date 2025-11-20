#include <stdio.h>      // printf, scanf, fopen, fscanf
#include <stdlib.h>     // malloc, free, exit
#include <string.h>     // memset
#include <math.h>       // factorial, pow (si lo quieres)

// ----------------------------------------------------
// ESTRUCTURAS BASE
// ----------------------------------------------------
int** tipoArco;  // tipoArco[u][v] = tipo leído del archivo

typedef struct Node Node;

// Lista de adyacencia
typedef struct AdjNode {
    Node* dest;
    struct AdjNode* next;
} AdjNode;

struct Node {
    int id;
    int color;      // 0 = blanco, 1 = rojo
    int iter;
    int tpc;
    Node* p;        // nodo padre
    AdjNode* adj;   // lista de sucesores
    int t[4][4][4];
};

// Grafo
typedef struct {
    Node** nodos;
    int num_nodos;
} Graph;

// ----------------------------------------------------
// COLA
// ----------------------------------------------------

typedef struct NodoCola {
    Node* dato;
    struct NodoCola* sig;
} NodoCola;

typedef struct {
    NodoCola* frente;
    NodoCola* final;
} Q;

Q* crearQ() {
    Q* q = (Q*)malloc(sizeof(Q));
    q->frente = NULL;
    q->final = NULL;
    return q;
}

int Q_vacia(Q* q) {
    return q->frente == NULL;
}

void Q_insert(Q* q, Node* n) {
    NodoCola* nuevo = (NodoCola*)malloc(sizeof(NodoCola));
    nuevo->dato = n;
    nuevo->sig = NULL;
    if (q->final == NULL)
        q->frente = nuevo;
    else
        q->final->sig = nuevo;
    q->final = nuevo;
}

Node* Q_pop(Q* q) {
    if (Q_vacia(q)) return NULL;
    NodoCola* aux = q->frente;
    Node* n = aux->dato;
    q->frente = aux->sig;
    if (q->frente == NULL)
        q->final = NULL;
    free(aux);
    return n;
}

// ----------------------------------------------------
// FUNCIONES AUXILIARES
// ----------------------------------------------------

double factorial(int n) {
    if (n < 0) return 0;
    return tgamma(n + 1);
}

int comb(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;

    double r = factorial(n) / (factorial(k) * factorial(n - k));

    return (int)(r + 0.5);
}

int t(Node* a, Node* b) {
    return tipoArco[a->id][b->id];
}


// agregar arista (lista de adyacencia)
void agregarArista(Node* origen, Node* destino) {
    AdjNode* nuevo = (AdjNode*)malloc(sizeof(AdjNode));
    nuevo->dest = destino;
    nuevo->next = origen->adj;
    origen->adj = nuevo;
}

// ----------------------------------------------------
// FUNCIONES PRINCIPALES
// ----------------------------------------------------

void search_motif_driver(Graph* G);
void search_motif(Graph* G, Node* s, int iter);

// Función para imprimir la matriz de combinaciones de un nodo
void imprimir_combinaciones(Node* n) {
    printf("\n  Matriz t[x][y][z] para nodo %d:\n", n->id);
    int valores[6][3] = {
        {1, 0, 1},
        {2, 0, 2},
        {3, 0, 3},
        {1, 0, 2},
        {1, 0, 3},
        {2, 0, 3}
    };
    
    for (int i = 0; i < 6; i++) {
        int x = valores[i][0];
        int y = valores[i][1];
        int z = valores[i][2];
        if (n->t[x][y][z] > 0) {
            printf("    t[%d][%d][%d] = %d\n", x, y, z, n->t[x][y][z]);
        }
    }
}

// Función para contar el total de motifs en todos los nodos
int contar_motifs_totales(Graph* G) {
    int total = 0;
    int valores[6][3] = {
        {1, 0, 1},
        {2, 0, 2},
        {3, 0, 3},
        {1, 0, 2},
        {1, 0, 3},
        {2, 0, 3}
    };
    
    for (int i = 0; i < G->num_nodos; i++) {
        for (int j = 0; j < 6; j++) {
            int x = valores[j][0];
            int y = valores[j][1];
            int z = valores[j][2];
            total += G->nodos[i]->t[x][y][z];
        }
    }
    return total;
}

void search_motif_driver(Graph* G) {
    int iter = 1;
    int i, j;
    
    for (i = 0; i < G->num_nodos; i++) {
        // Reset colors antes de cada búsqueda
        for (j = 0; j < G->num_nodos; j++) {
            G->nodos[j]->color = 0;
        }
        search_motif(G, G->nodos[i], iter);
        iter++;
    }
    
    printf("\n========================================\n");
    printf("RESULTADOS FINALES\n");
    printf("========================================\n");
    
    // Imprimir resultados de cada nodo
    for (i = 0; i < G->num_nodos; i++) {
        imprimir_combinaciones(G->nodos[i]);
    }
    
    // Contar y mostrar total de motifs
    int total_motifs = contar_motifs_totales(G);
    printf("\n========================================\n");
    printf("TOTAL DE MOTIFS ENCONTRADOS: %d\n", total_motifs);
    printf("========================================\n");
}

void search_motif(Graph* G, Node* root, int iter) {

    // 1) Inicializar
    memset(root->t, 0, sizeof(root->t));  // Limpiar matriz de combinaciones
    root->p = NULL;
    root->color = 1;     // rojo (visitado)

    int n1 = 0, n2 = 0, n3 = 0;
    AdjNode* adj;
    Node* current_node;
    Q* q = crearQ();

    // 2) Primera pasada: procesar sucesores directos de root
    for (adj = root->adj; adj != NULL; adj = adj->next) {
        Node* n = adj->dest;

        if (n->color != 1) {      // no rojo
            n->tpc = t(root, n);     // tipo(root, n)

            if (n->tpc == 1) n1++;
            if (n->tpc == 2) n2++;
            if (n->tpc == 3) n3++;

            n->p = root;
            Q_insert(q, n);
        }
    }

    // 3) Calcular combinatorias iniciales S.t(x,0,y)
    root->t[1][0][1] = comb(n1, 2);
    root->t[2][0][2] = comb(n2, 2);
    root->t[3][0][3] = comb(n3, 2);
    root->t[1][0][2] = comb(n1 + n2, 2) - root->t[1][0][1] - root->t[2][0][2];
    root->t[1][0][3] = comb(n1 + n3, 2) - root->t[1][0][1] - root->t[3][0][3];
    root->t[2][0][3] = comb(n2 + n3, 2) - root->t[2][0][2] - root->t[3][0][3];

    // 4) Recorrido BFS y correcciones
    while (!Q_vacia(q)) {
        current_node = Q_pop(q);
        current_node->color = 1;       // marcar como rojo
        current_node->iter = iter;     // marcar con esta iteración

        for (adj = current_node->adj; adj != NULL; adj = adj->next) {
            Node* n = adj->dest;

            if (n->color != 1 && n->iter != iter) {
                if (n->p == current_node->p) {
                    // Caso: mismo padre
                    current_node->p->t[current_node->tpc][0][n->tpc]--;
                    current_node->p->t[current_node->tpc][t(current_node, n)][n->tpc]++;
                } else {
                    // Caso: distinto padre
                    current_node->p->t[current_node->tpc][t(current_node, n)][0]++;
                }
                
                n->p = current_node;
                n->color = 1;
                n->iter = iter;
                Q_insert(q, n);
            }
        }
    }

    free(q);

}

// ----------------------------------------------------
// MAIN — lectura desde archivo
// ----------------------------------------------------

int main() {
    int i;
    char nombreArchivo[100];
    printf("Ingrese el nombre del archivo del grafo: ");
    scanf("%s", nombreArchivo);

    FILE* f = fopen(nombreArchivo, "r");
    if (!f) {
        printf("Error: No se pudo abrir el archivo '%s'\n", nombreArchivo);
        return 1;
    }

    int num_nodos, num_aristas;
    fscanf(f, "%d %d", &num_nodos, &num_aristas);

    printf("\nGrafo cargado exitosamente:\n");
    printf("  Nodos: %d\n", num_nodos);
    printf("  Aristas: %d\n\n", num_aristas);

    Graph G;
    G.num_nodos = num_nodos;
    G.nodos = (Node**)malloc(sizeof(Node*) * num_nodos);
    tipoArco = malloc((num_nodos + 1) * sizeof(int*));
    
    for (i = 0; i <= num_nodos; i++) {
        tipoArco[i] = calloc(num_nodos + 1, sizeof(int));
    }

    for (i = 0; i < num_nodos; i++) {
        G.nodos[i] = (Node*)malloc(sizeof(Node));
        G.nodos[i]->id = i + 1;
        G.nodos[i]->color = 0;
        G.nodos[i]->iter = 0;
        G.nodos[i]->tpc = 0;
        G.nodos[i]->p = NULL;
        G.nodos[i]->adj = NULL;
        memset(G.nodos[i]->t, 0, sizeof(G.nodos[i]->t));
    }

    printf("Leyendo aristas...\n");
    for (i = 0; i < num_aristas; i++) {
        int origen, destino, tipo;
        fscanf(f, "%d %d %d", &origen, &destino, &tipo);

        if (origen > 0 && origen <= num_nodos && destino > 0 && destino <= num_nodos) {
            tipoArco[origen][destino] = tipo;
            agregarArista(G.nodos[origen - 1], G.nodos[destino - 1]);
            printf("  Arista %d -> %d (tipo %d)\n", origen, destino, tipo);
        } else {
            printf("  Error: Arista inválida %d -> %d\n", origen, destino);
        }
    }
    fclose(f);

    search_motif_driver(&G);

    // Liberar memoria
    for (i = 0; i < G.num_nodos; i++) {
        AdjNode* adj = G.nodos[i]->adj;
        while (adj != NULL) {
            AdjNode* temp = adj;
            adj = adj->next;
            free(temp);
        }
        free(G.nodos[i]);
    }
    free(G.nodos);
    
    for (i = 0; i <= num_nodos; i++) {
        free(tipoArco[i]);
    }
    free(tipoArco);

    printf("\nPrograma finalizado.\n");
    return 0;
}

// Created by benja on 21-10-2025.
//