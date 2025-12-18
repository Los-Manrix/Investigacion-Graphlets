# 🔬 Investigación de Graphlets

Sistema para análisis de grafos y detección de motifs estructurales.

## 🚀 Inicio Rápido

```bash
python3 main.py
```

El sistema verifica e instala dependencias automáticamente.

## 📋 Funcionalidades

### 🔄 Conversores de Matrices
- **TFLink → Kavosh**: Convierte archivos TFLink a formato Kavosh
- **Kavosh → FormatoP**: Convierte a formato procesado
- **Kavosh → G-Trie**: Convierte a formato G-Trie
- **Pipeline Completa**: Ejecuta todas las conversiones

### 📊 Resultados
- `RESULTADOS-GTRIES.md`: Resultados de análisis con G-Trie
- `RESULTADOS-KAVOSH.md`: Resultados de análisis con Kavosh

## 📁 Estructura

```
├── main.py                      # Sistema completo (menú + utilidades + verificación)
├── Conversores_de_matrices/     # Scripts de conversión
├── Kavosh/                      # Herramienta Kavosh
├── gtrieScanner_src_01/         # Herramienta G-Trie
├── TOYS/                        # Datasets de prueba
├── README.md                    # Este archivo
├── RESULTADOS-GTRIES.md         # Resultados G-Trie
└── RESULTADOS-KAVOSH.md         # Resultados Kavosh
```

## 🔧 Requisitos

- Python 3.8+
- polars (se instala automáticamente si falta)

## 📖 Uso

```bash
python3 main.py
```

1. **Primera ejecución**: Instala dependencias si es necesario
2. **Seleccionar opción** del menú
3. **Seguir instrucciones** de cada herramienta

## 🎯 Navegación

- Números `[1-9]`: Seleccionar opción
- `[T]`: Pipeline completa
- `[V]`: Volver
- `[0]`: Salir

## 📄 Documentación

- Ver archivos `RESULTADOS-*.md` para detalles de análisis
- Cada conversor tiene su propio README en su carpeta

## 🔗 Repositorio

**Los-Manrix/Investigacion-Graphlets** - Branch: Resultados
