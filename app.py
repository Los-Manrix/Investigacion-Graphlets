from conversionFormato import conversion_formato as conv
from nuevoOrdenamiento import Nuevo_Ordenamiento as new_ord

def main():
    conv.run()
    print("Conversion terminada...")
    new_ord.run()
    print("Ordenamiento terminado...")
    print("Proceso terminado")
    return

if __name__ == '__main__':
    main()
