import os

n_nodos = 0
arcos_a = []


def index(file: str, index: str) -> void:
    global n_nodos
    global arcos
    global arcos_a

    dic = {}
    with open (file, 'r') as f:
        contenido = f.read()
        abc_arcos = []
        abc_nodos = contenido.split()
        set_abc = set(abc_nodos)
        counter = 1

        for line in f:
            abc_arcos.append(line.split())

        for i in set_abc:
            new_data = {i: counter}
            dic.update(new_data)
            counter += 1

    with open(index, 'w') as i:
        i.write("Index  ID\n\n")
        for key in dic.keys():
            i.write(f"{dic[key]}      {key}\n")

    n_nodos = len(abc_nodos)
    arcos_a = abc_arcos

    return dic


def conversion(file: str, matrix: str, i_dic: dict) -> void:
    final = []
    with open(file, 'r') as f:
        for i in arcos_a[1:len(abc)]:
            final.append([i_dic[i[0]], i_dic[i[1]]])

    with open(matrix, 'w') as m:
        m.write(f"{n_nodos}\n")
        m.write(f"{len(final)}\n")
        for i in final:
            m.write(f"{i[0]}        {i[1]}\n")

    return


def run() -> void:
    ruta = '../networks/weird/'
    counter = 0
    for file in os.listdir(ruta):
        ruta_comp = os.path.join(ruta, file)
        if os.path.isfile(ruta_comp):
            i_dic = index(ruta_comp, f"../index/index{counter}.txt")
            conversion(ruta_comp, f"../networks/standards/matrix{counter}.txt", i_dic)
            counter += 1
    return
