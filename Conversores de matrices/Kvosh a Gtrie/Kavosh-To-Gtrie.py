import sys
from pathlib import Path

# -------------------------------
# RUTAS BASE
# -------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

KAVOSH_INPUT_DIR = BASE_DIR / "TOYS" / "Kavosh"
GTRIE_TOYS_OUTPUT_DIR = BASE_DIR / "TOYS" / "G-trieScanner"
GTRIE_NETWORKS_OUTPUT_DIR = BASE_DIR / "gtrieScanner_src_01" / "networks"


# -------------------------------
# CONVERSIÓN DE FORMATO
# -------------------------------
def convert_to_gtrie_format(input_path: Path, output_path: Path):
    """
    Convierte un archivo Kavosh (A B) al formato G-Trie (A B 1),
    ignorando la primera línea.
    """
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    if len(lines) <= 1:
        raise ValueError("El archivo no contiene suficientes líneas.")

    pairs = [line.strip().split() for line in lines[1:] if line.strip()]

    out_lines = []
    for pair in pairs:
        if len(pair) >= 2:
            out_lines.append(f"{pair[0]} {pair[1]} 1")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))


# -------------------------------
# MENÚ
# -------------------------------
def show_menu(files):
    print("\nArchivos disponibles para convertir:\n")
    for i, file in enumerate(files, start=1):
        print(f"[{i}] {file.name}")
    print("\n[A] Convertir TODOS")
    print("[0] Salir\n")


def get_user_choice(max_value):
    while True:
        choice = input("Selecciona una opción: ").strip()

        if choice.lower() == "a":
            return "ALL"

        try:
            choice = int(choice)
            if 0 <= choice <= max_value:
                return choice
        except ValueError:
            pass

        print("Entrada inválida. Intenta nuevamente.")


# -------------------------------
# CONVERSIÓN MASIVA
# -------------------------------
def convert_all(files):
    converted = 0
    skipped = 0

    print("\n🔄 Convirtiendo todos los archivos...\n")

    for file in files:
        output_name = file.stem + "_converted.txt"
        out_toys = GTRIE_TOYS_OUTPUT_DIR / output_name
        out_networks = GTRIE_NETWORKS_OUTPUT_DIR / output_name

        if out_toys.exists() or out_networks.exists():
            print(f"⏭️  Saltado (ya convertido): {file.name}")
            skipped += 1
            continue

        try:
            convert_to_gtrie_format(file, out_toys)
            convert_to_gtrie_format(file, out_networks)
            print(f"✅ Convertido: {file.name}")
            converted += 1
        except Exception as e:
            print(f"❌ Error en {file.name}: {e}")

    print("\n📊 Resumen:")
    print(f"  • Convertidos: {converted}")
    print(f"  • Saltados:    {skipped}")
    print("✔️ Proceso finalizado.")


# -------------------------------
# MAIN
# -------------------------------
def main():
    if not KAVOSH_INPUT_DIR.exists():
        print(f"❌ No se encontró el directorio: {KAVOSH_INPUT_DIR}")
        sys.exit(1)

    kavosh_files = sorted(KAVOSH_INPUT_DIR.glob("*.txt"))

    if not kavosh_files:
        print("❌ No se encontraron archivos .txt en TOYS/Kavosh")
        sys.exit(1)

    show_menu(kavosh_files)
    choice = get_user_choice(len(kavosh_files))

    if choice == 0:
        print("Saliendo...")
        sys.exit(0)

    # -------------------------------
    # OPCIÓN: TODOS
    # -------------------------------
    if choice == "ALL":
        convert_all(kavosh_files)
        sys.exit(0)

    # -------------------------------
    # OPCIÓN: UNO SOLO
    # -------------------------------
    selected_file = kavosh_files[choice - 1]
    output_name = selected_file.stem + "_converted.txt"

    output_toys_path = GTRIE_TOYS_OUTPUT_DIR / output_name
    output_networks_path = GTRIE_NETWORKS_OUTPUT_DIR / output_name

    if output_toys_path.exists() or output_networks_path.exists():
        print("\n⚠️  Este archivo ya fue convertido anteriormente.")
        print(f"📄 Archivo: {selected_file.name}")
        print("❌ No se realizará ninguna conversión.")
        sys.exit(0)

    print(f"\n📄 Archivo seleccionado: {selected_file.name}")
    print("🔄 Convirtiendo...\n")

    try:
        convert_to_gtrie_format(selected_file, output_toys_path)
        convert_to_gtrie_format(selected_file, output_networks_path)
    except Exception as e:
        print(f"❌ Error durante la conversión: {e}")
        sys.exit(1)

    print("✅ Conversión completada con éxito.")
    print("📁 Guardado en:")
    print(f"  • {output_toys_path}")
    print(f"  • {output_networks_path}")


if __name__ == "__main__":
    main()
