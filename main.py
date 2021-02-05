from classes import *

monto_maximo = 100000
default_path = "prestamo.csv"

def main(arg = None):
    print("Banco 3000".center(75,'-'))
    if empty_file(default_path):
        with open(default_path,'w') as f:
            csvwrite = csv.writer(f)
            csvwrite.writerow(columnas)
    print("".center(75,'-'))
    if arg == None:
        while True:
            opt = int(input("\n1) Iniciar sesion 2) Registro => "))
            while opt != 1 and opt != 2:
                opt = int(input("1) Iniciar sesion 2) Registro => "))
            print("".center(75,'-'))
            if opt == 1:
                user = input("Ingrese el primer nombre y primer apellido => ").split()
                row = search(default_path,user[0],user[1])
                if row != None:
                    if checkPassword(row):
                        print("Usuario encontrado".center(75,'-'))
                        user = prestamo(row[0],row[1],[row[2],row[3]],[row[4],row[5]],row[6],row[7],row[8],row[9],row[10],row[11])
                        user.imprimir_usuario()
                        print("Usuario encontrado".center(75,'-'))
                        print("Fecha y Hora del nuevo prestamo:")
                        user.recargarFecha()
                        user.recargarTiempo()
                        break
                    else:
                        print("Password incorrecto")
                else:
                    print("Usuario no encontrado".center(75,'-'))
            else:
                user = prestamo()
                break
    else:
        user = arg
        print("Usuario encontrado".center(75,'-'))
        print("Fecha y Hora del nuevo prestamo:")
        user.recargarFecha()
        user.recargarTiempo()
    if user.verificarFecha():
        if user.num_prestamo < 6:
            print("".center(75,'-'))
            user.crearPrestamo()
            if user.dinero_prestado < monto_maximo: 
                user.crearPlazos()
                user.guardar = True
            else:
                print("".center(75,'-'))
                print("Exedes el monto maximo a prestar")
        else:
            print("".center(75,'-'))
            print("Supero el limite de prestamos")
    else:
        print("".center(75,'-'))
        print("Solo hacemos prestamos los primeros 20 dias del mes")
    opt = int(input("Desea imprimir los datos del prestamo= 1) SI 2) NO => "))
    if opt == 1:
        user.imprimirPrestamo()
    opt = int(input("Desea hacer ingresar otro prestamo? 1) SI 2) NO => "))
    if opt == 1:
        opt = int(input("Desea usar el mismo usuario o cambiarlo? 1) SI 2) NO => "))
        if opt == 1:
            main(user)
        else:
            main()

if __name__ == "__main__":
    main()