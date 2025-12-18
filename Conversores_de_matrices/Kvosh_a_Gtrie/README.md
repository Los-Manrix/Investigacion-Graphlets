# Kavosh To G-Trie Converter

## Descripción

Este script convierte archivos de redes en formato Kavosh al formato requerido por
G-Trie Scanner.

Convierte aristas del tipo:

A B

al formato:

A B 1

El conversor:
- Escanea automáticamente la carpeta TOYS/Kavosh
- Muestra un menú interactivo para elegir el archivo a convertir
- Genera archivos con sufijo _converted.txt
- Copia automáticamente el resultado a las carpetas necesarias para G-Trie

---

## Estructura esperada del repositorio

El script asume la siguiente estructura:

TOYS/
├── Kavosh/
│   └── *.txt
├── G-trieScanner/

gtrieScanner_src_01/
└── networks/

---

## Uso

Desde la carpeta del conversor:

python3 Kavosh-To-Gtrie.py

El programa mostrará un menú como:

[1] TCGA-BRCA-elbow-GRN.txt  
[2] TFLink_Homo_sapiens_interactions_LS_simpleFormat_v1.0.tsv.txt  
[0] Salir  

Selecciona el número del archivo que deseas convertir.

---

## Salida

Para un archivo de entrada como:

TCGA-BRCA-elbow-GRN.txt

Se generará automáticamente:

TCGA-BRCA-elbow-GRN_converted.txt

El archivo convertido se guardará en:

- TOYS/G-trieScanner/
- gtrieScanner_src_01/networks/

---

## Control de duplicados

Si el archivo convertido ya existe, el script mostrará un aviso y no sobrescribirá
los datos:

⚠️ Este archivo ya fue convertido anteriormente.

---

## Requisitos

- Python 3.8 o superior
- No requiere librerías externas

---

## Notas

- El script ignora la primera línea del archivo de entrada.
- Solo procesa archivos .txt.
- Pensado para facilitar experimentos comparativos entre Kavosh y G-Trie.
