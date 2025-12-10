# Reporte de Resultados: Kavosh

Nota: en este reporte llamamos "hub" a un nodo con grado muy alto (muchas conexiones). Los hubs suelen ser puntos centrales en la red que facilitan la difusión y mantienen la conectividad; su presencia afecta la estructura y la distribución de motifs.

## Ejecución: TCGA-BRCA-elbow-GRN (Motif Size 3)

**Comando:** `./Kavosh -i networks/TCGA-BRCA-elbow-GRN.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 19,251
*   **Aristas (Conexiones):** 322,840
*   **Grado Máximo:** 5,096
*   **Distribución de Grados:** La red tiene nodos altamente conectados (hubs) y muchos con pocas conexiones.
    *   *(El **Grado** indica cuántas conexiones tiene un nodo. Por ejemplo, hay 43 nodos con solo 1 conexión, mientras que un nodo tiene 5096 conexiones).*

### Resultados
*   **Subgrafos Totales:** 152,654,393
*   **Motifs:** 13
*   **Tiempo Total:** 51.23 segundos

---

## Ejecución: TCGA-OV-elbow-GRN (Motif Size 3)

**Comando:** `./Kavosh -i networks/TCGA-OV-elbow-GRN.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 19,249
*   **Aristas (Conexiones):** 339,136
*   **Grado Máximo:** 2,476
*   **Distribución de Grados:** Similar a la anterior, con hubs importantes (grado máx 2476) y muchos nodos de bajo grado.
    *   *(Ejemplo: 44 nodos con grado 1, 247 con grado 2).*

### Resultados
*   **Subgrafos Totales:** 129,007,119
*   **Motifs:** 13
*   **Tiempo Total:** 42.69 segundos

---

## Ejecución: TFLink_Caenorhabditis_elegans_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Caenorhabditis_elegans_interactions_LS_simpleFormat_v1.0.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 16,529
*   **Aristas (Conexiones):** 315,827
*   **Grado Máximo:** 7,719
*   **Distribución de Grados:** Muchos nodos con grado bajo y algunos hubs; por ejemplo, 2,914 nodos con grado 1.

### Resultados
*   **Subgrafos Totales:** 553,828,787
*   **Motifs:** 13
*   **Tiempo Total:** 180.86 segundos

---

## Ejecución: TFLink_Danio_rerio_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Danio_rerio_interactions_LS_simpleFormat_v1.0.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 13,773
*   **Aristas (Conexiones):** 25,955
*   **Grado Máximo:** 9,026
*   **Distribución de Grados:** Muchísimos nodos con grado 1 (6,448); hay pocos hubs con grado muy alto (ej. grado máximo 9,026).

### Resultados
*   **Subgrafos Totales:** 65,793,468
*   **Motifs:** 4
*   **Tiempo Total:** 23.75 segundos

---

## Ejecución: TFLink_Drosophila_melanogaster_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Drosophila_melanogaster_interactions_LS_simpleFormat_v1.0.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 18,766
*   **Aristas (Conexiones):** 367,875
*   **Grado Máximo:** 12,717
*   **Distribución de Grados:** Muchos nodos con bajo grado y algunos hubs extremos (grado máximo 12,717).

### Resultados
*   **Subgrafos Totales:** 1,140,552,890
*   **Motifs:** 13
*   **Tiempo Total:** 392.78 segundos

---



## Ejecución: TFLink_Rattus_norvegicus_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Rattus_norvegicus_interactions_LS_simpleFormat_v1.0.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 13,546
*   **Aristas (Conexiones):** 81,215
*   **Grado Máximo:** 9,565
*   **Distribución de Grados:** Muchos nodos de bajo grado y algunos hubs; grado máximo 9,565.

### Resultados
*   **Subgrafos Totales:** 261,052,796
*   **Motifs:** 11
*   **Tiempo Total:** 88.30 segundos

---

## Ejecución: TFLink_Saccharomyces_cerevisiae_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Saccharomyces_cerevisiae_interactions_LS_simpleFormat_v1.0.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 6,555
*   **Aristas (Conexiones):** 232,250
*   **Grado Máximo:** 5,478
*   **Distribución de Grados:** Muchos nodos con grado bajo y algunos hubs (grado máximo 5,478).

### Resultados
*   **Subgrafos Totales:** 253,562,168
*   **Motifs:** 13
*   **Tiempo Total:** 83.94 segundos

---

## Ejecución: TFLink_Homo_sapiens_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Homo_sapiens_interactions_LS_simpleFormat_v1.0.tsv.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 20,128
*   **Aristas (Conexiones):** 6,722,146
*   **Grado Máximo:** 19,235
*   **Distribución de Grados:** Red muy grande con muchos nodos de bajo grado y algunos hubs de grado extremo.

### Resultados
*   **Subgrafos Totales:** En ejecución (no disponible)
*   **Motifs:** En ejecución (no disponible)
*   **Tiempo Total:** En ejecución (>1 hora al momento del registro)

---

## Ejecución: TFLink_Mus_musculus_interactions_LS (Motif Size 3)

**Comando:** `./Kavosh -i networks/TFLink_Mus_musculus_interactions_LS_simpleFormat_v1.0.tsv.txt -s 3`

### Estadísticas de la Red
*   **Nodos:** 21,338
*   **Aristas (Conexiones):** 4,048,589
*   **Grado Máximo:** 19,091
*   **Distribución de Grados:** Red grande con muchos nodos de bajo grado y algunos hubs extremos.

### Resultados
*   **Subgrafos Totales:** En ejecución (no disponible)
*   **Motifs:** En ejecución (no disponible)
*   **Tiempo Total:** En ejecución (>1 hora al momento del registro)

---

