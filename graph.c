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

void search_motif_driver(Graph* G) {
    int iter = 1;
    int i;
    for (i = 0; i < G->num_nodos; i++) {
        search_motif(G, G->nodos[i], iter);
        iter++;
    }
}

void search_motif(Graph* G, Node* s, int iter) {

    // 1) Inicializar
    memset(s->t, 0, sizeof(s->t));
    Q* q = crearQ();
    s->p = NULL;
    s->color = 1;     // rojo

    int n1 = 0, n2 = 0, n3 = 0;
    AdjNode* adj;

    // 2) Primera pasada: procesar sucesores directos de s
    for (adj = s->adj; adj != NULL; adj = adj->next) {

        Node* n = adj->dest;

        if (n->color != 1) {      // n no rojo
            n->tpc = t(s, n);     // tipo(s,n)

            if (n->tpc == 1) n1++;
            if (n->tpc == 2) n2++;
            if (n->tpc == 3) n3++;

            n->p = s;
            Q_insert(q, n);
        }
    }
    printf("%i\n",n1);
    printf("%i\n",n2);
    printf("%i\n",n3);

    // 3) S.t(x,0,y) combinatorias iniciales
    int t11 = comb(n1, 2);
    int t22 = comb(n2, 2);
    int t33 = comb(n3, 2);

    s->t[1][0][1] = t11;
    s->t[2][0][2] = t22;
    s->t[3][0][3] = t33;

    s->t[1][0][2] = comb(n1 + n2, 2) - t11 - t22;
    s->t[1][0][3] = comb(n1 + n3, 2) - t11 - t33;
    s->t[2][0][3] = comb(n2 + n3, 2) - t22 - t33;




    // 4) Recorrido BFS y correcciones
    while (!Q_vacia(q)) {

        s = Q_pop(q);
        s->iter = iter;
        s->color = 1;             // ahora es rojo

        for (adj = s->adj; adj != NULL; adj = adj->next) {

            Node* n = adj->dest;

            if (n->color != 1 && n->iter != iter) {

                if (n->p == s->p) {

                    // caso igual
                    s->p->t[s->tpc][0][n->tpc]--;
                    s->p->t[s->tpc][ t(s,n) ][n->tpc]++;

                } else {

                    // caso distinto
                    s->p->t[s->tpc][ t(s,n) ][0]++;
                }
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
        printf("No se pudo abrir el archivo '%s'\n", nombreArchivo);
        return 1;
    }

    int num_nodos, num_aristas;
    fscanf(f, "%d %d", &num_nodos, &num_aristas);

    Graph G;
    G.num_nodos = num_nodos;
    G.nodos = (Node**)malloc(sizeof(Node*) * num_nodos);
    tipoArco = malloc((num_nodos + 1) * sizeof(int*));
    for (i = 1; i <= num_nodos; i++) {
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


    }

    for (i = 0; i < num_aristas; i++) {
        int origen, destino, tipo;
        fscanf(f, "%d %d %d", &origen, &destino, &tipo);


        tipoArco[origen][destino] = tipo;
        agregarArista(G.nodos[origen - 1], G.nodos[destino - 1]);
    }
    fclose(f);

    search_motif_driver(&G);


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

    return 0;
}

// Created by benja on 21-10-2025.
//