class fecha:
    dia = None
    mes = None
    anio = None
    def __init__(self,*arg):
        if len(arg) == 0:
            self.dia = int(input("Dia => "))
            self.mes = int(input("Mes => "))
            self.anio = int(input("Anio => "))
        elif len(arg) == 1 and isinstance(arg[0],str):
            ffecha = arg[0].split("-")
            self.dia = int(ffecha[0])
            self.mes = int(ffecha[1])
            self.anio = int(ffecha[2])
        elif len(arg) == 3 and isinstance(arg[0],int) and isinstance(arg[1],int) and isinstance(arg[2],int):
            self.dia = arg[0]
            self.mes = arg[1]
            self.anio = arg[2]
        self._actualizar()

    def imprimir_fecha(self):
        print(str(self.dia)+"-"+str(self.mes)+"-"+str(self.anio))

    def es_bisiesto(self,anio: int) -> bool:
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

    def _actualizar(self):
        if self.mes == 2 and self.dia > 27 and not self.es_bisiesto(self.anio):
            self.dia -= 27
            self.mes += 1
            self._actualizar()
        elif self.mes == 2 and self.dia > 28 and self.es_bisiesto(self.anio):
            self.dia -= 28
            self.mes += 1
            self._actualizar()
        elif self.mes in [1,3,5,7,8,10,12] and self.dia > 31:
            self.dia -= 31
            self.mes += 1
            self._actualizar()
        elif self.mes in[2,4,6,9,11] and self.dia > 30:
            self.dia -= 30
            self.mes += 1
            self._actualizar()
        if self.mes > 12:
            self.anio += 1
            self.mes -= 12
            self.dia = 1
            self._actualizar()

    def suma(self,*arg):
        auxFecha = fecha(self.dia,self.mes,self.anio)
        if len(arg) == 1:
            auxFecha.dia += arg[0]
        elif len(arg) == 2:
            auxFecha.dia += arg[0]
            auxFecha.mes += arg[1]
        elif len(arg) == 3:
            auxFecha.dia += arg[0]
            auxFecha.mes += arg[1]
            auxFecha.anio += arg[2]
        auxFecha._actualizar()
        return auxFecha
    
    

class prestamo(fecha):
    plazos = 0
    def __init__(self):
        print("Fecha del prestamos")
        fecha.__init__(self)

    def verificarFecha(self) -> bool:
        return self.dia > 21
    
    def crearPlazos(self,tplazos):
        print("Plazos de pago")
        ffecha = fecha(self.dia,self.mes,self.anio)
        for x in range(tplazos):
            ffecha = ffecha.suma(30)
            ffecha.imprimir_fecha()


class persona:
    nombre = None
    apellidos = None
    genero = None
    curp = None
    tel_movil = None
    tel_casa = None
    __password = None
    def __init__(self,*arg):
        if len(arg) == 0:
            self.nombre = input("Nombre(s) => ").split()
            self.apellidos = input("Apellidos => ").split()
            self.genero = input("Genero => ")
            self.curp = input("CURP => ")
            # Ingreso de datos int
            self.tel_movil = int(input("Telefono movil => "))
            self.tel_casa = int(input("Telefono de casa => "))
            self.password = int(input("Password (Solo numeros) => "))
    #@dispatch((str,list,tuple),(list,tuple),str,int)
        elif len(arg) == 4:
            self.nombre = arg[0]
            self.apellidos = arg[1]
            self.curp = arg[2]
            self.password = arg[3]
    def imprimir_usuario(self):
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
