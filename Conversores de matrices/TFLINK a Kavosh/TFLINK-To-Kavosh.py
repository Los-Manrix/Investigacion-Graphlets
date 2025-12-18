import sys
from pathlib import Path
from typing import List, Tuple
import polars as pl


# Directorios base detectados desde la ubicacion del script
BASE_DIR = Path(__file__).resolve().parents[2]
# Entrada: archivos TFLink dentro de TOYS/TFLINK
TFLINK_INPUT_DIR = BASE_DIR / "TOYS" / "TFLINK"
# Salidas Kavosh en TOYS y en la carpeta Kavosh/networks
TOYS_KAVOSH_DIR = BASE_DIR / "TOYS" / "Kavosh"
KAVOSH_NETWORKS_DIR = BASE_DIR / "Kavosh" / "networks"


def read_pairs_from_tflink(input_path: Path) -> List[Tuple[str, str]]:
    """Lee un archivo TFLink y devuelve una lista de pares (TF, Target).

    Intenta detectar columnas comunes ('UniprotID.TF', 'UniprotID.Target', 'TF', 'Target').
    Si no detecta nombres, toma las dos primeras columnas de cada fila.
    """
    # Intentar leer con polars como TSV primero
    try:
        df = pl.read_csv(str(input_path), separator="\t", has_header=True, infer_schema_length=0, low_memory=True)
    except Exception:
        # fallback: leer como texto y parsear líneas
        pairs: List[Tuple[str, str]] = []
        with open(input_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    pairs.append((parts[0], parts[1]))
        return pairs

    cols_lower = [c.lower() for c in df.columns]

    # Buscar columnas conocidas (prioridad)
    if "uniprotid.tf" in cols_lower and "uniprotid.target" in cols_lower:
        a = df[df.columns[cols_lower.index("uniprotid.tf")]].to_list()
        b = df[df.columns[cols_lower.index("uniprotid.target")]].to_list()
        return list(zip(a, b))

    if "tf" in cols_lower and "target" in cols_lower:
        a = df[df.columns[cols_lower.index("tf")]].to_list()
        b = df[df.columns[cols_lower.index("target")]].to_list()
        return list(zip(a, b))

    # Si hay al menos 2 columnas, tomar las dos primeras
    if len(df.columns) >= 2:
        a = df[df.columns[0]].to_list()
        b = df[df.columns[1]].to_list()
        return list(zip(a, b))

    # Último recurso: iterar filas y tomar dos primeros tokens
    pairs: List[Tuple[str, str]] = []
    for row in df.rows():
        parts = [str(x) for x in row if x is not None]
        if len(parts) >= 2:
            pairs.append((parts[0], parts[1]))
    return pairs


def write_kavosh_file(output_path: Path, pairs: List[Tuple[str, str]]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for a, b in pairs:
            f.write(f"{a} {b}\n")
    print(f"Escrito: {output_path} ({len(pairs)} arcos)")


def show_menu(files: List[Path]) -> None:
    print("\nArchivos disponibles para convertir (TFLink -> Kavosh):\n")
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
    base = input_file.stem
    out_toys = TOYS_KAVOSH_DIR / f"{base}.txt"
    out_kavosh = KAVOSH_NETWORKS_DIR / f"{base}.txt"

    try:
        pairs = read_pairs_from_tflink(input_file)
        if not pairs:
            return False, f"No se encontraron pares en {input_file.name}"

        write_kavosh_file(out_toys, pairs)
        write_kavosh_file(out_kavosh, pairs)
        return True, f"Convertido: {input_file.name} -> {out_toys} and {out_kavosh}"
    except Exception as e:
        return False, f"Error: {e}"


def convert_all(files: List[Path]) -> None:
    converted = 0
    skipped = 0
    print("\n🔄 Convirtiendo todos los archivos TFLink...\n")
    for file in files:
        out_toys = TOYS_KAVOSH_DIR / f"{file.stem}.txt"
        out_kavosh = KAVOSH_NETWORKS_DIR / f"{file.stem}.txt"
        if out_toys.exists() or out_kavosh.exists():
            print(f"⏭️ Saltado (ya existe): {file.name}")
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
    if not TFLINK_INPUT_DIR.exists():
        print(f"❌ No se encontró el directorio de entrada: {TFLINK_INPUT_DIR}")
        return
    files = sorted(TFLINK_INPUT_DIR.glob("*.txt"))
    if not files:
        print("❌ No se encontraron archivos .txt en TOYS/TFLINK")
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
    out_toys = TOYS_KAVOSH_DIR / f"{selected.stem}.txt"
    out_kavosh = KAVOSH_NETWORKS_DIR / f"{selected.stem}.txt"
    if out_toys.exists() or out_kavosh.exists():
        print(f"\n⚠️  {selected.name} ya fue convertido (se encontró salida).")
        return
    print(f"\n📄 Archivo seleccionado: {selected.name}")
    print("🔄 Convirtiendo...\n")
    ok, msg = convert_single(selected)
    if ok:
        print("✅ Conversión completada.")
        print(f"  • {TOYS_KAVOSH_DIR / (selected.stem + '.txt')}")
        print(f"  • {KAVOSH_NETWORKS_DIR / (selected.stem + '.txt')}")
    else:
        print(f"❌ {msg}")


if __name__ == "__main__":
    main()