#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MAX_NODES 50000
#define MAX_QUEUE 50000
#define DEBUG 0
#define VERBOSE 0
#define DBG_PAUSE if(DEBUG) getchar()
#define VRB_PRINT(...) if(VERBOSE) printf(__VA_ARGS__)

unsigned long long int nexpansions = 0; 

struct snode;
typedef struct snode snode;

struct snode //search nodes
{
  int id;
  short color;
  unsigned iter;
  unsigned nsuccs;
  short tpc;
  snode *parent;
};

struct AdjListNode {
    int dest;
    int type;
    struct AdjListNode* next;
};

struct Graph {
    int V;
    struct AdjListNode** array;
};

struct Graph* graph;
snode* searchNodes[MAX_NODES];
snode* queue[MAX_QUEUE];

int front = 0;
int rear = 0;

void clear_queue(){
	front = 0;
	rear = 0;
}


int empty_queue(){
	return (rear >= front);
}
void queue_insert(snode* node){
	queue[front++] = node;
}
snode* queue_pop(){
	return queue[rear++]; 
}

// Function to create a new adjacency list node
struct AdjListNode* newAdjListNode(int dest,int type) {
    struct AdjListNode* newNode = malloc(sizeof(struct AdjListNode));
    newNode->dest = dest;
    newNode->type = type;
    newNode->next = NULL;
    return newNode;
}

// Function to create a graph of V vertices
struct Graph* createGraph(int V) {
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->V = V;
    graph->array = calloc(V, sizeof(struct AdjListNode*));
    return graph;
}

// Function to add an edge to an undirected graph
void addEdge(struct Graph* graph, int src, int dest, int type) {
    
    // Add an edge from src to dest
    struct AdjListNode* node = newAdjListNode(dest,type);
    node->next = graph->array[src];
    graph->array[src] = node;

    // Since the graph is undirected, add an edge from dest to src
   /* node = newAdjListNode(src);
    node->next = graph->array[dest];
    graph->array[dest] = node;*/
}

// Function to print the adjacency list
void printGraph(struct Graph* graph) {
    int i;
    struct AdjListNode* cur;
	for (i = 0; i < graph->V; i++) {
        VRB_PRINT("%d: nsuccs:%d", i,searchNodes[i]->nsuccs);
        for (cur = graph->array[i]; cur; cur = cur->next) {
            VRB_PRINT(" [%d %d]", cur->dest,cur->type);
        }
        VRB_PRINT("\n");
    }
}

snode* new_SearchNode(int id) {
    snode* node = (snode*)malloc(sizeof(snode));
  	node->id = id;
  	node->color = 0;
  	node->iter = 0;
  	node->tpc = 0;
  	node->nsuccs = 0;
	node->parent = NULL;
    return node;
}

void initializeSearchNodes() {
    int i;
    struct AdjListNode* cur;
	for (i = 0; i < graph->V; i++) {
        searchNodes[i] = new_SearchNode(i); 
    }
}

void ReadGraph(const char* filename) {
	FILE* f;
	int i, ori, dest, dist, t, num_gnodes,num_arcs;
	f = fopen(filename, "r");
	if (f == NULL) 	{
		printf("Cannot open file %s.\n", filename);
		exit(1);
	}
	fscanf(f, "%d %d", &num_gnodes, &num_arcs);
	fscanf(f, "\n");
	printf("%d %d %d\n", num_gnodes, num_arcs,INT_MAX);
	DBG_PAUSE;
	graph = createGraph(num_gnodes);
	initializeSearchNodes();
	for (i = 0; i < num_arcs; i++) {

		fscanf(f, "%d %d %d\n", &ori, &dest, &t);
		if(ori-1==dest-1){
			continue;
		}
		addEdge(graph, ori-1, dest-1, t);
		searchNodes[ori-1]->nsuccs++;
	//	printf("%d %d %d %d\n", ori, dest, dist, t);
	}
	fclose(f);
}

long long int type[4][4][4];
void initialize_type(){
	int i,j,k;
	for(i = 0;i < 4;i++)
		for(j = 0;j < 4;j++)
			for(k = 0;k < 4;k++)
				type[i][j][k] = 0;
}


void print_types(){
	int i,j,k;
	long long int total = 0;
	for(i = 0;i < 4;i++)
		for(j = 0;j < 4;j++)
			for(k = 0;k < 4;k++){
				printf("[%d][%d][%d] : %lld\n",i,j,k,type[i][j][k]);
				total += type[i][j][k]; //< 0 ? -type[i][j][k] : type[i][j][k];
			}
	printf("Total subgrafos: %lld\n", total);
}


/**
 * Calcula la combinatoria C(n,2) = n*(n-1)/2
 * Usa desplazamiento de bits (>> 1) para dividir por 2
 */
long long comb2(int n) {
    if (n < 2) return 0;
    return ((long long)n * (n - 1)) >> 1;
}


void search_motif(snode* node, int iter){
	int n1 = 0, n2 = 0, n3 = 0; //n1 succ, n2 pred, n3 ambos
	node->parent = NULL;
	node->color = 1; //1 is red
	struct AdjListNode* cur;
	//printf("\n current node %d\n", node->id);

	//printf("antes n1:%d comb2(n1):%d n2:%d n3:%d - %d %d %d %d %d %d\n",n1,comb2(n1),n2,n3,type[1][0][1],type[2][0][2],type[3][0][3],type[1][0][2],type[1][0][3],type[2][0][3]);		
	    
	for (cur = graph->array[node->id]; cur; cur = cur->next) {     
	//		printf(" [%d %d]", cur->dest,cur->type);
		
		snode* succ = searchNodes[cur->dest]; 
		
		if (succ->color != 1){
			nexpansions++;
			succ->tpc = cur->type;
			if (succ->tpc == 1)
				n1++;
			if (succ->tpc == 2)
				n2++;
			if (succ->tpc == 3)
				n3++;
			succ->parent = node;
			queue_insert(succ);
			//printf("Insert node %d\n", succ->id);
		}				
    }
	type[1][0][1] += comb2(n1); //1 
	type[2][0][2] += comb2(n2); //0 
	type[3][0][3] += comb2(n3); //0
	type[1][0][2] += comb2(n1 + n2) - comb2(n1) - comb2(n2); //1 - 1 - 0 = 0
	type[1][0][3] += comb2(n1 + n3) - comb2(n1) - comb2(n3); //3 - 1 - 0 = 2
	type[2][0][3] += comb2(n2 + n3) - comb2(n2) - comb2(n3); //0 - 0 - 0 = 0
	if (type[1][0][1] > INT_MAX){
		VRB_PRINT("llego %d\n",INT_MAX);
//	getchar();
	}

    if (type[1][0][1] > LLONG_MAX || type[1][0][1] < 0){
		VRB_PRINT("llego %lld\n",LLONG_MAX);
		DBG_PAUSE;
	}


	VRB_PRINT("n1:%d comb2(n1):%lld n2:%d n3:%d - %lld %lld %lld %lld %lld %lld\n",n1,comb2(n1),n2,n3,type[1][0][1],type[2][0][2],type[3][0][3],type[1][0][2],type[1][0][3],type[2][0][3]);
	DBG_PAUSE;
	while (!(empty_queue())){
		snode* s = queue_pop();
		s->iter = iter;
		VRB_PRINT("  Pop node %d\n", s->id);
		for (cur = graph->array[s->id]; cur; cur = cur->next) {

			snode* n = searchNodes[cur->dest];
			if (n->color != 1 && n->iter != iter){
				nexpansions++;
				//printf("    See node %d\n", n->id);
				if (n->parent == s->parent){
					int ta = s->tpc, tb = n->tpc;
					if (ta > tb) { int tmp = ta; ta = tb; tb = tmp; }
					VRB_PRINT("Se resta 1 a [%d][%d][%d]\n",ta,0,tb);
					VRB_PRINT("Se agrega 1 a [%d][%d][%d]\n",s->tpc,cur->type,n->tpc);
					type[ta][0][tb]--;
					type[s->tpc][cur->type][n->tpc]++;
					//if (type[s->tpc][0][n->tpc] < 0)
						DBG_PAUSE;
				}else{
					//printf("False Se agrega 1 a [%d][%d][%d]\n",s->tpc,cur->type,0);
					type[s->tpc][cur->type][0]++;
				}
					
			}
			
		}
 
	}
	//getchar();
}

void search_motif_driver(){
	int i,iter = 1;
	struct AdjListNode* cur;
	initialize_type();
	int maxnumbersucc = 0;
	for (i = 0; i < graph->V; i++) {
        VRB_PRINT("%d: nsuccs:%d %lld\n", i,searchNodes[i]->nsuccs,type[1][0][1]);
        if (maxnumbersucc < searchNodes[i]->nsuccs)
          maxnumbersucc = searchNodes[i]->nsuccs;
		search_motif(searchNodes[i], iter);
        //getchar();
		iter++;
		clear_queue();
	}
	print_types();
	printf("maxnumbersucc:%d\n",maxnumbersucc);
}
/*
for all s belong to G
	search_motif(s, iter)
	iter++
}*/

/*
int main() {
	printf("comb2(1): %lld\n",comb2(1));
	getchar();
	//ReadGraph("./Benchmarks/outs/TFLink_Danio_rerio_interactions_LS_simpleFormat_v1.0_procesado.txt");
    //ReadGraph("yeast_procesado_carlos.txt");
	//ReadGraph("3graph_procesado.txt");
	ReadGraph("./Investigacion-Graphlets/TOYS/FormatoP/12nodos_grafo_doble_procesado.txt");
	//ReadGraph("TFLink_Homo_sapiens.txt");
	//ReadGraph("TFLink_Danio_rerio_interactions_LS_simpleFormat_v1.0_procesado.txt");
	//ReadGraph("TFLink_Rattus_norvegicus_interactions_LS_simpleFormat_v1.0_procesado.txt");
//	ReadGraph("TFLink_Mus_musculus_interactions_LS_simpleFormat_v1.0.tsv_procesado.txt");
//	ReadGraph("TFLink_Drosophila_melanogaster_interactions_LS_simpleFormat_v1.0_procesado.txt");

	search_motif_driver();
	
    printf("nexpansions: %llu\n", nexpansions);
   // printGraph(graph);

    return 0;
}
*/
int main(int argc, char *argv[]) {
    printf("comb2(1): %lld\n", comb2(1));
    DBG_PAUSE;

    if (argc < 2) {
        fprintf(stderr, "Uso: %s <archivo_grafo>\n", argv[0]);
        return 1;
    }

    ReadGraph(argv[1]);

    clock_t t_inicio = clock();
    search_motif_driver();
    clock_t t_fin = clock();

    printf("nexpansions: %llu\n", nexpansions);
    printf("Tiempo busqueda: %.6f segundos\n", (double)(t_fin - t_inicio) / CLOCKS_PER_SEC);
    return 0;
}
