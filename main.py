from classes import *

monto_maximo = 10000

def main():
    #"Claudio Hassiel","Araujo Palestina","Masculino","CPA34253P",58675472,87968434,1234
    x = prestamo()
    if x.verificarFecha():
        x.crearPrestamo()
        if x.dinero_prestado <= monto_maximo:
            x.imprimirPrestamo()
        else:
            print("Excede los limites de nuestro bando")
    else:
        print("Solo hay prestamos los primeros 20 dias del mes")

if __name__ == "__main__":
    main()