import os
import csv

n_nodos = 0
arcos_a = []


def index(file: str, index_file: str) -> dict:
    global n_nodos
    global arcos_a

    dic = {}
    abc_arcos = []
    abc_nodos = []

    with open(file, 'r') as f:
        f.seek(0)
        lector = csv.reader(f, delimiter='\t')
        counter = 1

        for line in lector:
            if len(line) >= 2:
                abc_arcos.append([line[0], line[1]])
                abc_nodos.append(line[0])
                abc_nodos.append(line[1])
        set_abc = set(abc_nodos)

        for nodo in set_abc:
            dic[nodo] = counter
            counter += 1

    with open(index_file, 'w') as i:
        i.write("Index  ID\n\n")
        for key, value in dic.items():
            i.write(f"{value}      {key}\n")

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
