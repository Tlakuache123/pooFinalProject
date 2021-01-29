class persona:
    def __init__(self):
        print("Ingrese los datos del usuario")
        self.nombre = input("Nombre del usuario => ")
        self.apellidoP,self.apellidoM = input("Apellidos (paterno materno) => ").split()
        self.numCasa = int(input("Telefono de casa => "))
        self.numCel = int(input("Numero celular => "))
        self.corre = input("Correo electronico => ")
        self.genero = input("Genero => ")
        self.nacimiento = input("Fecha de nacimiento (YYYY-MM-DD) => ")
        self.contrasena = input("Contrasena => ")

class prestamo(persona):
    def __init__(self):
        persona.__init__(self)
        print("Ingrese los datos del prestamo")
        self.numPrestamo = int(input("Numero de prestamo => "))
        self.valor = float(input("Valor del presamo => "))