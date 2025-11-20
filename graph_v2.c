#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NODES 2000

// Estructura para conteo: [TipoOrigen][TipoCierre][TipoDestino]
long long global_motif_counts[4][4][4];

// Grafo
int adjMatrix[MAX_NODES][MAX_NODES];
typedef struct Node
{
    int id;
    int type;
    struct Node *next;
} Node;
Node *adjList[MAX_NODES];

// Propiedades de cada nodo durante la búsqueda
typedef struct
{
    int parent;
    int tpc;
    int iter;
    int color;
} NodeProps;

NodeProps props[MAX_NODES];

// Estructura auxiliar para vecinos
typedef struct
{
    int id;
    int type;
} NeighborInfo;

// Cola
NeighborInfo queue[MAX_NODES];
int q_front, q_rear;

void addEdge(int u, int v, int type)
{
    adjMatrix[u][v] = type;
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->id = v;
    newNode->type = type;
    newNode->next = adjList[u];
    adjList[u] = newNode;
}

long long comb2(int n)
{
    if (n < 2)
        return 0;
    return ((long long)n * (n - 1)) / 2;
}

void search_motif(int s, int iter)
{
    // s.p = NULL
    props[s].parent = -1;
    // s.color = red
    props[s].color = 1;

    // Contadores por tipo
    int n1 = 0, n2 = 0, n3 = 0;

    // Reiniciar cola
    q_front = q_rear = 0;

    // for all succ n belong to s do
    Node *curr = adjList[s];
    while (curr != NULL)
    {
        int n = curr->id;
        int tpc = curr->type;

        // if n.color != red
        if (props[n].color != 1)
        {
            // n.tpc = t(s, n)
            props[n].tpc = tpc;

            if (tpc == 1)
                n1++;
            if (tpc == 2)
                n2++;
            if (tpc == 3)
                n3++;

            // n.p = s
            props[n].parent = s;

            // Q.insert(n)
            queue[q_rear].id = n;
            queue[q_rear].type = tpc;
            q_rear++;
        }

        curr = curr->next;
    }

    
    global_motif_counts[1][0][1] += comb2(n1);
    global_motif_counts[2][0][2] += comb2(n2);
    global_motif_counts[3][0][3] += comb2(n3);
    global_motif_counts[1][0][2] += comb2(n1 + n2) - comb2(n1) - comb2(n2);
    global_motif_counts[1][0][3] += comb2(n1 + n3) - comb2(n1) - comb2(n3);
    global_motif_counts[2][0][3] += comb2(n2 + n3) - comb2(n2) - comb2(n3);

    // While (Q != empty)
    while (q_front < q_rear)
    {
        // s = Q.pop
        int node = queue[q_front].id;
        int node_tpc = queue[q_front].type;
        q_front++;

        // s.iter = iter
        props[node].iter = iter;

        // for all succ n belong to s do
        Node *succ = adjList[node];
        while (succ != NULL)
        {
            int n = succ->id;
            int edge_type = succ->type; // tipo(s, n)

            // if n.color != red && n.iter != iter
            if (props[n].parent == props[node].parent)
            {
                int n_tpc = props[n].tpc;

                if (node_tpc <= n_tpc)
                {
                    global_motif_counts[node_tpc][0][n_tpc]--;
                    global_motif_counts[node_tpc][edge_type][n_tpc]++;
                }
                else
                {
                    global_motif_counts[n_tpc][0][node_tpc]--;
                    global_motif_counts[n_tpc][edge_type][node_tpc]++;
                }
            }
            else
            {
                // s.p.t(s.tpc, tipo(s,n), 0)++
                global_motif_counts[node_tpc][edge_type][0]++;
            }

            succ = succ->next;
        }
    }
}

void search_motif_driver(int max_id)
{
    int iter = 1;

    // for all s belong to G
    for (int s = 0; s <= max_id; s++)
    {
        // search_motif(s, iter)
        search_motif(s, iter);
        // iter++
        iter++;
    }
}

int main()
{
    char filename[] = "graph_procesado.txt";

    FILE *file = fopen(filename, "r");
    if (!file)
    {
        printf("Error: No se encuentra %s\n", filename);
        return 1;
    }

    // Limpieza
    memset(adjMatrix, 0, sizeof(adjMatrix));
    memset(global_motif_counts, 0, sizeof(global_motif_counts));
    memset(props, 0, sizeof(props));
    for (int i = 0; i < MAX_NODES; i++)
    {
        adjList[i] = NULL;
        props[i].color = 0;
        props[i].parent = -1;
    }

    int num_nodes, num_edges;
    if (fscanf(file, "%d %d", &num_nodes, &num_edges) != 2)
        return 1;

    int u, v, t, max_id = 0;
    while (fscanf(file, "%d %d %d", &u, &v, &t) == 3)
    {
        if (u < MAX_NODES && v < MAX_NODES)
        {
            addEdge(u, v, t);
            if (u > max_id)
                max_id = u;
            if (v > max_id)
                max_id = v;
        }
    }
    fclose(file);

    // Ejecutar driver
    search_motif_driver(max_id);

    // Imprimir
    printf("Procesando archivo: %s\n", filename);
    printf("--- Cantidad de Motifs---\n");

    long long total_motifs = 0;
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 0; j <= 3; j++)
        {
            for (int k = 1; k <= 3; k++)
            {
                long long val = global_motif_counts[i][j][k];
                if (val > 0)
                {
                    printf("(%d, %d, %d) : %lld\n", i, j, k, val);
                    total_motifs += val;
                }
            }
        }
    }

    printf("--------------------------\n");
    printf("Total Motifs: %lld\n", total_motifs);

    return 0;
}