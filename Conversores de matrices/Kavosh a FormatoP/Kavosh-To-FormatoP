from pathlib import Path
from typing import Tuple, List, Set


# Directorios base detectados desde la ubicacion del script
BASE_DIR = Path(__file__).resolve().parents[2]
# Entrada: archivos Kavosh en TOYS/Kavosh
KAVOSH_INPUT_DIR = BASE_DIR / "TOYS" / "Kavosh"
# Salida: archivos procesados (FormatoP) en TOYS/FormatoP
FORMATOP_OUTPUT_DIR = BASE_DIR / "TOYS" / "FormatoP"


def procesar_pares(input_path: Path) -> Tuple[int, List[Tuple[int, int]], Set[Tuple[int, int]]]:
    """
    Lee un archivo de matriz Kavosh y clasifica los pares (a,b) según su aparición:
    - Tipo 1/2: par único y su inverso
    - Tipo 3: pares bidireccionales (aparecen ambos sentidos)
    Retorna (num_nodos, unidireccionales, bidireccionales).
    """
    pares: Set[Tuple[int, int]] = set()
    bidireccionales: Set[Tuple[int, int]] = set()

    with open(input_path, "r", encoding="utf-8") as f:
        primera = f.readline().strip()
        if not primera.isdigit():
            raise ValueError(f"La primera línea de {input_path.name} no es un número válido de nodos.")
        num_nodos = int(primera)

        for linea in f:
            partes = linea.strip().split()
            if len(partes) < 2:
                continue

            a, b = int(partes[0]), int(partes[1])

            if (b, a) in pares:
                bidireccionales.add((a, b))
                bidireccionales.add((b, a))
            pares.add((a, b))

    # Tipos 1/2 = los pares que no son bidireccionales
    unidireccionales = [p for p in pares if p not in bidireccionales]

    return num_nodos, unidireccionales, bidireccionales


def escritura(output_path: Path, num_nodos: int, unidireccionales: List[Tuple[int, int]], bidireccionales: Set[Tuple[int, int]]) -> None:
    """Escribe el archivo procesado en formato FormatoP."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    buffer = []

    # Unidireccionales (1 y 2)
    for a, b in unidireccionales:
        buffer.append(f"{a}     {b}     1\n")
        buffer.append(f"{b}     {a}     2\n")

    # Bidireccionales (3)
    for a, b in bidireccionales:
        buffer.append(f"{a}     {b}     3\n")

    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write(f"{num_nodos}   {len(buffer)}\n")
        f_out.writelines(buffer)

    print(f"Escrito: {output_path} ({len(buffer)} líneas)")


def show_menu(files: List[Path]) -> None:
    print("\nArchivos disponibles para convertir (Kavosh -> FormatoP):\n")
    for i, file in enumerate(files, start=1):
        print(f"[{i}] {file.name}")
    print("\n[A] Convertir TODOS")
    print("[0] Salir\n")


def get_user_choice(max_value: int):
    while True:
        choice = input("Selecciona una opción: ").strip()
        if choice.lower() == "a":
            return "ALL"
        try:
            choice_int = int(choice)
            if 0 <= choice_int <= max_value:
                return choice_int
        except ValueError:
            pass
        print("Entrada inválida. Intenta nuevamente.")


def convert_single(input_file: Path) -> Tuple[bool, str]:
    """Convierte un archivo Kavosh a FormatoP."""
    base = input_file.stem
    output_path = FORMATOP_OUTPUT_DIR / f"{base}_procesado.txt"

    try:
        num_nodos, uni, bi = procesar_pares(input_file)
        escritura(output_path, num_nodos, uni, bi)
        return True, f"Convertido: {input_file.name} -> {output_path.name}"
    except Exception as e:
        return False, f"Error procesando {input_file.name}: {e}"


def convert_all(files: List[Path]) -> None:
    converted = 0
    skipped = 0
    print("\n🔄 Convirtiendo todos los archivos Kavosh a FormatoP...\n")

    for file in files:
        output_path = FORMATOP_OUTPUT_DIR / f"{file.stem}_procesado.txt"
        if output_path.exists():
            print(f"⏭️  Saltado (ya existe): {file.name}")
            skipped += 1
            continue

        ok, msg = convert_single(file)
        if ok:
            print(f"✅ {msg}")
            converted += 1
        else:
            print(f"❌ {msg}")

    print("\n📊 Resumen:")
    print(f"  • Convertidos: {converted}")
    print(f"  • Saltados:    {skipped}")
    print("✔️ Finalizado.")


def main():
    if not KAVOSH_INPUT_DIR.exists():
        print(f"❌ No se encontró el directorio de entrada: {KAVOSH_INPUT_DIR}")
        return

    files = sorted(KAVOSH_INPUT_DIR.glob("*.txt"))
    if not files:
        print(f"❌ No se encontraron archivos .txt en {KAVOSH_INPUT_DIR}")
        return

    show_menu(files)
    choice = get_user_choice(len(files))

    if choice == 0:
        print("Saliendo...")
        return

    if choice == "ALL":
        convert_all(files)
        return

    selected = files[choice - 1]
    output_path = FORMATOP_OUTPUT_DIR / f"{selected.stem}_procesado.txt"

    if output_path.exists():
        print(f"\n⚠️  {selected.name} ya fue convertido (se encontró salida).")
        print(f"📄 Archivo: {output_path}")
        print("❌ No se realizará ninguna conversión.")
        return

    print(f"\n📄 Archivo seleccionado: {selected.name}")
    print("🔄 Convirtiendo...\n")

    ok, msg = convert_single(selected)
    if ok:
        print("✅ Conversión completada con éxito.")
        print(f"📁 Guardado en: {output_path}")
    else:
        print(f"❌ {msg}")


if __name__ == "__main__":
    main()