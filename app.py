import time
from conversionFormato import conversion_formato as conv
from nuevoOrdenamiento import Nuevo_Ordenamiento as new_ord

def main():
    start_time = time.time()
    conv.run()
    print("Conversion terminada...")
    new_ord.run()
    print("Ordenamiento terminado...")
    print("Proceso terminado")
    end_time = time.time()
    print(f"tiempo total: {end_time - start_time:.4f} segundos")
    return

if __name__ == '__main__':
    main()
