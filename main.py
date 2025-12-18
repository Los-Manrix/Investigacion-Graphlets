"""
Sistema centralizado para el proyecto de Investigación de Graphlets.
Punto de entrada principal con menús organizados.

Uso: python3 main.py
"""
import os
import sys
import subprocess
from pathlib import Path
from typing import Optional, List

# Agregar directorio raíz al path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))


# ============================================================================
# VERIFICACIÓN DE DEPENDENCIAS
# ============================================================================

def verificar_polars():
    """Verifica e instala polars si es necesario."""
    try:
        import polars
        return True
    except ImportError:
        print("\n⚠️  La librería 'polars' no está instalada")
        print("    Es necesaria para los conversores TFLink → Kavosh\n")
        resp = input("¿Instalar ahora? (s/n): ").strip().lower()
        
        if resp in ['s', 'si', 'sí', 'y', 'yes']:
            print("\n🔧 Instalando polars...")
            try:
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", "polars", "--quiet"
                ])
                print("✅ Polars instalado exitosamente\n")
                return True
            except:
                print("❌ Error instalando polars")
                print("   Instala manualmente: pip install polars\n")
                return False
        else:
            print("\n⚠️  Algunas funcionalidades no estarán disponibles")
            input("Presiona ENTER para continuar...")
            return False


# ============================================================================
# UTILIDADES DE MENÚ
# ============================================================================

def limpiar_pantalla():
    """Limpia la pantalla de la terminal."""
    os.system('clear' if os.name != 'nt' else 'cls')


def mostrar_titulo(titulo: str, ancho: int = 60):
    """Muestra un título formateado."""
    print("\n" + "=" * ancho)
    print(titulo.center(ancho))
    print("=" * ancho + "\n")


def obtener_opcion(prompt: str = "Selección: ", validas: Optional[List[str]] = None) -> str:
    """Obtiene y valida una opción del usuario."""
    while True:
        opcion = input(prompt).strip().upper()
        
        if not opcion:
            print("⚠️  Opción vacía. Intenta de nuevo.\n")
            continue
            
        if validas is None or opcion in validas:
            return opcion
        
        print(f"⚠️  Opción '{opcion}' no válida. Intenta de nuevo.\n")


def confirmar_accion(mensaje: str = "¿Continuar?") -> bool:
    """Pide confirmación al usuario."""
    respuesta = input(f"\n{mensaje} (s/n): ").strip().lower()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']


def pausa(mensaje: str = "\nPresiona ENTER para continuar..."):
    """Pausa la ejecución hasta que el usuario presione ENTER."""
    input(mensaje)


# ============================================================================
# MENÚS DEL SISTEMA
# ============================================================================


def menu_conversores():
    """Menú de conversores de matrices."""
    # Importar conversores solo cuando se necesiten
    from Conversores_de_matrices.Kavosh_a_FormatoP import Kavosh_to_FormatoP
    from Conversores_de_matrices.Kvosh_a_Gtrie import Kavosh_to_Gtrie
    from Conversores_de_matrices.TFLINK_a_Kavosh import TFLINK_to_Kavosh
    
    while True:
        limpiar_pantalla()
        mostrar_titulo("� CONVERSORES DE MATRICES")
        
        print("  [1] TFLink → Kavosh")
        print("  [2] Kavosh → FormatoP")
        print("  [3] Kavosh → G-Trie")
        print("  [T] Pipeline Completa (TODO)")
        print()
        print("  [V] Volver al menú principal")
        print("  [0] Salir")
        print()
        
        opcion = obtener_opcion(validas=['1', '2', '3', 'T', 'V', '0'])
        
        if opcion == '0':
            if confirmar_accion("¿Salir del programa?"):
                print("\n👋 ¡Hasta luego!\n")
                sys.exit(0)
        elif opcion == 'V':
            return
        elif opcion == '1':
            limpiar_pantalla()
            mostrar_titulo("TFLink → Kavosh")
            try:
                TFLINK_to_Kavosh.main()
            except Exception as e:
                print(f"\n❌ Error: {e}")
            pausa()
        elif opcion == '2':
            limpiar_pantalla()
            mostrar_titulo("Kavosh → FormatoP")
            try:
                Kavosh_to_FormatoP.main()
            except Exception as e:
                print(f"\n❌ Error: {e}")
            pausa()
        elif opcion == '3':
            limpiar_pantalla()
            mostrar_titulo("Kavosh → G-Trie")
            try:
                Kavosh_to_Gtrie.main()
            except Exception as e:
                print(f"\n❌ Error: {e}")
            pausa()
        elif opcion == 'T':
            limpiar_pantalla()
            mostrar_titulo("🔄 Pipeline Completa")
            print("Ejecutando conversiones en secuencia...\n")
            try:
                print("1/3: TFLink → Kavosh")
                TFLINK_to_Kavosh.main()
                print("\n2/3: Kavosh → FormatoP")
                Kavosh_to_FormatoP.main()
                print("\n3/3: Kavosh → G-Trie")
                Kavosh_to_Gtrie.main()
                print("\n✅ Pipeline completada exitosamente")
            except Exception as e:
                print(f"\n❌ Error: {e}")
            pausa()


def menu_principal():
    """Menú principal del sistema."""
    while True:
        limpiar_pantalla()
        print("\n" + "="*60)
        print("🔬 INVESTIGACIÓN DE GRAPHLETS".center(60))
        print("="*60)
        print("\n  Sistema de Gestión y Análisis de Grafos\n")
        print("="*60 + "\n")
        
        print("  [1] 🔄 Conversores de Matrices")
        print("  [2] � Ver Resultados")
        print("  [0] Salir")
        print()
        
        opcion = obtener_opcion(validas=['1', '2', '0'])
        
        if opcion == '0':
            if confirmar_accion("¿Salir del programa?"):
                print("\n👋 ¡Hasta luego!\n")
                break
        elif opcion == '1':
            menu_conversores()
        elif opcion == '2':
            limpiar_pantalla()
            mostrar_titulo("📊 RESULTADOS")
            print("\n📄 Archivos de resultados disponibles:\n")
            print("  • RESULTADOS-GTRIES.md")
            print("  • RESULTADOS-KAVOSH.md\n")
            print(f"📁 Ubicación: {BASE_DIR}\n")
            pausa()


if __name__ == "__main__":
    # Verificar dependencias
    verificar_polars()
    
    # Ejecutar menú principal
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido.\n")
        sys.exit(0)