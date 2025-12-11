def convert_to_cp_format(input_path, output_path):
    """
    Convierte un archivo con pares (A B) al formato (A B 1),
    saltándose la primera línea del archivo.
    """
    with open(input_path, "r") as f:
        lines = f.read().strip().splitlines()

    # Saltar la primera línea
    pairs = [line.strip().split() for line in lines[1:]]

    # Convertir al formato A B 1
    out_lines = [f"{a} {b} 1" for a, b in pairs]

    # Guardar resultado
    with open(output_path, "w") as f:
        f.write("\n".join(out_lines))

    print(f"Conversión completa.\nArchivo guardado como: {output_path}")


# -------------------------------
# EJEMPLO DE USO
# -------------------------------
input_file = "TFLink_Drosophila_melanogaster_interactions_LS_simpleFormat_v1.0.txt"          # Archivo de entrada
output_file = "TFLink_Drosophila_melanogaster_interactions_LS_simpleFormat_v1.0_converted.txt"  # Archivo de salida

convert_to_cp_format(input_file, output_file)
