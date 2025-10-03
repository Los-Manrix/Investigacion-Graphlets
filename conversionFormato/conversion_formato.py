import os
import polars as pl

n_nodos = 0
arcos_a = []


def index(file: str, index_file: str) -> dict:
    global n_nodos
    global arcos_a

    df = pl.read_csv(
        file, 
        separator="\t",
        has_header=True,
        infer_schema_length=0,
        null_values=["-", "~", ""],
        low_memory=True
    )

    df_reduced = df.select(["UniprotID.TF", "UniprotID.Target"])
    
    col0 = df_reduced["UniprotID.TF"]
    col1 = df_reduced["UniprotID.Target"]

    abc_arcos = list(zip(col0, col1))
    abc_nodos = col0 + col1
    set_abc = set(abc_nodos)

    dic = {nodo: i+1 for i, nodo in enumerate(set_abc)}

    print("Lectura lista...")

    with open(index_file, "w") as i:
        i.write("Index\tID\n\n")
        for key, value in dic.items():
            i.write(f"{value}\t{key}\n")

    n_nodos = len(set_abc)
    arcos_a = abc_arcos

    return dic


def conversion(file: str, matrix_file: str, i_dic: dict) -> None:
    final = []

    for arco in arcos_a:
        if arco[0] in i_dic and arco[1] in i_dic:
            final.append([i_dic[arco[0]], i_dic[arco[1]]])

    with open(matrix_file, 'w') as m:
        m.write(f"{n_nodos}\n")
        m.write(f"{len(final)}\n")
        for i in final:
            m.write(f"{i[0]}        {i[1]}\n")



def run() -> None:
    ruta = './networks/weird'
    counter = 0

    for file in os.listdir(ruta):
        ruta_comp = os.path.join(ruta, file)
        if os.path.isfile(ruta_comp):
            i_dic = index(ruta_comp, f"./index/index{counter}.txt")
            conversion(ruta_comp, f"./networks/standards/matrix{counter}.txt", i_dic)
            counter += 1
