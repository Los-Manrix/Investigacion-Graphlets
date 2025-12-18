# 🔬 Investigación de Graphlets

Sistema para análisis de grafos y detección de motifs estructurales (graphlets).

Herramientas incluidas:
- **Kavosh**: Algoritmo ESU para detección de motifs
- **gtrieScanner**: Análisis optimizado con G-Tries
- **Conversores**: TFLink ↔ Kavosh ↔ FormatoP ↔ G-Trie

---

## ⚠️ IMPORTANTE: Crear Entorno Virtual

### � **SIEMPRE USA ENTORNO VIRTUAL**

**¿Por qué?** Para aislar las dependencias del proyecto y no contaminar tu Python global.

### 📦 Instalación Paso a Paso:

```bash
# 1. Clonar el repositorio
git clone https://github.com/Los-Manrix/Investigacion-Graphlets.git
cd Investigacion-Graphlets
git checkout Resultados

# 2. ⭐ CREAR ENTORNO VIRTUAL (MUY IMPORTANTE) ⭐
python3 -m venv .venv

# 3. ACTIVAR el entorno virtual
# En Linux/Mac:
source .venv/bin/activate

# En Windows:
.venv\Scripts\activate

# Verás (.venv) al inicio de tu terminal cuando esté activo

# 4. Instalar dependencias (si las hay)
pip install polars

# 5. Ejecutar el sistema
python3 main.py
```

### 🔴 Desactivar entorno virtual (cuando termines):
```bash
deactivate
```

---

## 🚀 Uso Rápido (después de activar .venv)

```bash
python3 main.py
```

El sistema verifica e instala dependencias automáticamente si faltan.

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

- **Python 3.8+**
- **Entorno virtual** (.venv) ⚠️ OBLIGATORIO
- **polars** (se instala automáticamente)

## 📖 Flujo de Trabajo

### Primera vez:
```bash
# 1. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# o .venv\Scripts\activate en Windows

# 2. Ejecutar
python3 main.py
```

### Siguientes veces:
```bash
# 1. Activar entorno (SIEMPRE)
source .venv/bin/activate  # verás (.venv) en el prompt

# 2. Ejecutar
python3 main.py

# 3. Al terminar
deactivate
```

### Uso del menú:
1. Selecciona una opción (número o letra)
2. Sigue las instrucciones en pantalla
3. `[V]` para volver, `[0]` para salir

## 🎯 Navegación del Menú

| Tecla | Acción |
|-------|--------|
| `1-9` | Seleccionar opción |
| `T` | Ejecutar Pipeline completa |
| `V` | Volver al menú anterior |
| `0` | Salir del programa |

## 📄 Documentación

### Resultados de Análisis:
- 📊 `RESULTADOS-GTRIES.md` - Resultados con G-Trie Scanner
- 📊 `RESULTADOS-KAVOSH.md` - Resultados con Kavosh

### Conversores:
Cada conversor tiene su README en su carpeta:
- `Conversores_de_matrices/TFLINK_a_Kavosh/`
- `Conversores_de_matrices/Kavosh_a_FormatoP/`
- `Conversores_de_matrices/Kvosh_a_Gtrie/`

### Herramientas:
- `Kavosh/` - Implementación y documentación
- `gtrieScanner_src_01/` - Implementación y documentación

## 🐛 Solución de Problemas

### Error: "No module named 'polars'"
```bash
# Asegúrate de tener el entorno virtual activo
source .venv/bin/activate
pip install polars
```

### Error: "python3: command not found"
```bash
# En algunos sistemas usa:
python main.py
```

### ¿Cómo sé si el entorno virtual está activo?
Verás `(.venv)` al inicio de tu prompt:
```bash
(.venv) usuario@pc:~/proyecto$
```

## 👥 Contribuir

1. Fork el proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcionalidad`)
3. **Activa el entorno virtual** antes de trabajar
4. Commit tus cambios (`git commit -m 'Agregar funcionalidad'`)
5. Push a la rama (`git push origin feature/nueva-funcionalidad`)
6. Abre un Pull Request

## 📝 Licencia

Ver archivos LICENSE en directorios `Kavosh/` y `gtrieScanner_src_01/`

## 🔗 Repositorio

**GitHub**: [Los-Manrix/Investigacion-Graphlets](https://github.com/Los-Manrix/Investigacion-Graphlets)  
**Branch**: `Resultados`

---

### ⚠️ RECORDATORIO: Siempre activa el entorno virtual antes de trabajar
```bash
source .venv/bin/activate
```
