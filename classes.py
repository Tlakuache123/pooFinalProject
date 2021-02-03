from multipledispatch import dispatch

class fecha:
    dia = None
    mes = None
    anio = None
    @dispatch()
    def __init__(self):
        self.dia = input("Dia => ")
        self.mes = input("Mes => ")
        self.anio = input("Anio => ")
    @dispatch(int,int,int)
    #Ejemplo => fecha(22,05,2001)
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    #Ejemplo => fecha(22-05-2001)
    @dispatch(str)
    def __init__(self,ffecha):
        realFecha = ffecha.split("-")
        self.dia = int(realFecha[0])
        self.mes = int(realFecha[1])
        self.anio = int(realFecha[2])
    def imprimir(self):
        print(str(self.dia)+"-"+str(self.mes)+"-"+str(self.anio))

class persona:
    nombre = None
    apellidos = None
    genero = None
    curp = None
    tel_movil = None
    tel_casa = None
    __password = None
    @dispatch()
    def __init__(self):
        self.nombre = input("Nombre(s) => ").split()
        self.apellidos = input("Apellidos => ").split()
        self.genero = input("Genero => ")
        self.curp = input("CURP => ")
        # Ingreso de datos int
        self.tel_movil = int(input("Telefono movil => "))
        self.tel_casa = int(input("Telefono de casa => "))
        self.password = int(input("Password (Solo numeros) => "))
    @dispatch((str,list,tuple),(list,tuple),str,int)
    def __init__(self,nombre,apellidos,curp,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.curp = curp
        self.password = password
    def printInfo(self):
        print("Informacion del usuario".center(75,'-'))
        print("Nombre(s):".ljust(25),end="")
        print(" ".join(self.nombre).center(50))
        print("Apellidos:".ljust(25),end="")
        print(" ".join(self.apellidos).center(50))
        print("Genero:".ljust(25),end="")
        print(str(self.genero).center(50))
        print("CURP:".ljust(25),end="")
        print(self.curp.center(50))
        print("Telf-movil:".ljust(25),end="")
        print(str(self.tel_movil).center(50))
        print("Telf-casa:".ljust(25),end="")
        print(str(self.tel_casa).center(50))
        print("".center(75,'-'))