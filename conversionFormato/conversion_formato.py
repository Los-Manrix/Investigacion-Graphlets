import os
import polars as pl


def index(file: str, index_file: str):
    df = pl.read_csv(
        file, 
        separator="\t",
        has_header=True,
        infer_schema_length=0,
        null_values=["-", "~", ""],
        low_memory=True
    )

    df_reduced = df.select(["UniprotID.TF", "UniprotID.Target"])
    col0 = df_reduced["UniprotID.TF"].to_list()
    col1 = df_reduced["UniprotID.Target"].to_list()

    abc_arcos = list(zip(col0, col1))
    abc_nodos = col0 + col1
    set_abc = set(abc_nodos)

    # Crear diccionario de índices
    dic = {nodo: idx for idx, nodo in enumerate(set_abc, start=1)}

    print(f"Lectura lista: {len(set_abc)} nodos, {len(abc_arcos)} arcos")

    os.makedirs(os.path.dirname(index_file), exist_ok=True)
    with open(index_file, "w") as f:
        f.write("Index\tID\n")
        for key, value in dic.items():
            f.write(f"{value}\t{key}\n")

    return dic, abc_arcos, len(set_abc)


def conversion(matrix_file: str, arcos_a: list, i_dic: dict, n_nodos: int):
    os.makedirs(os.path.dirname(matrix_file), exist_ok=True)

    with open(matrix_file, "w") as m:
        m.write(f"{n_nodos}\n")
        m.write(f"{len(arcos_a)}\n")
        for a, b in arcos_a:
            m.write(f"{i_dic[a]}\t{i_dic[b]}\n")

    print(f"Archivo matriz escrito: {matrix_file}")


def run():
    ruta = './networks/weird'
    counter = 0

    os.makedirs("./index", exist_ok=True)
    os.makedirs("./networks/standards", exist_ok=True)

    for file in os.listdir(ruta):
        ruta_comp = os.path.join(ruta, file)
        if os.path.isfile(ruta_comp):
            nombre_base = os.path.splitext(os.path.basename(file))[0]
            salida = f"{nombre_base}"

            i_dic, arcos_a, n_nodos = index(ruta_comp, f"./index/index_{salida}.txt")
            conversion(f"./networks/standards/{salida}.txt", arcos_a, i_dic, n_nodos)
            counter += 1


if __name__ == "__main__":
    run()
