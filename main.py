from Conversores_de_matrices.Kavosh_a_FormatoP import Kavosh-To-FormatoP
from Conversores_de_matrices.Kavosh_a_GTrie import Kavosh-To-GTrie
from Conversores_de_matrices.TFLink_a_Kavosh import TFLink_To_Kavosh


def main():
    print("Selecciona que hacer: ")
    print("----------------------------")
    print("1) Kavosh a FormatoP")
    print("2) Kavosh a GTrie")
    print("3) TFLink a Kavosh")
    print("A) TODO")
    print("0) Salir")
    print("----------------------------")

    elec = str(input("Seleccion: "))

    if int(elec) is 1:
        Kavosh-To-FormatoP.main()
    elif int(elec) is 2:
        Kavosh-To-GTrie.main()
    elif int(elec) is 3:
        TFLink_a_Kavosh.main()
    elif elec is A:
        TFLink_a_Kavosh.main()
        Kavosh-To-FormatoP.main()
        Kavosh-To-GTrie.main()
    elif int(elec) is 0:
        return
    else:
        print("Formato invalido\n")
        main()


if __name__ == "__main__":
    main()

