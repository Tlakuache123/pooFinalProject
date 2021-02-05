class tiempo:
    minutos = 0
    horas = 0
    dias = 0
    dias = 0
    def __init__(self,*arg):
        if len(arg) == 0:
            htiempo = input("Ingrese el tiempo (MM:HH) => ").split(':')
            self.horas = htiempo[0]
            self.minutos = htiempo[1]
        elif len(arg) == 1 and isinstance(arg[0],str):
            htiempo = arg[0].split(':')
            self.horas = htiempo[0]
            self.minutos = htiempo[1]
        elif len(arg) == 2 and isinstance(arg[0],int) and isinstance(arg[0],int):
            self.horas = arg[0]
            self.minutos = arg[1]
        self._actualizar()

    def enviarDias(self):
        tdias = self.dias
        self.dias = 0
        return tdias

    def _actualizar(self):
        if self.minutos > 60:
            self.minutos -= 60
            self.horas += 1
            self._actualizar()
        if self.horas == 24 and self.minutos > 0:
            self.horas -= 24
            self.dias += 1
            self._actualizar()
        elif self.horas > 24:
            self.horas -= 24
            self.dias += 1
            self._actualizar()

    def sumaTiempo(self,*arg):
        tTiempo = tiempo(self.horas,self.minutos)
        if len(arg) == 1 and isinstance(arg[0],int):
            tTiempo.minutos += arg[0]
        elif len(arg) == 2  and isinstance(arg[0],int) and isinstance(arg[1],int):
            tTiempo.horas += arg[0]
            tTiempo.minutos += arg[1]
        elif len(arg) == 1 and isinstance(arg[0],str):
            rtTIempo = arg[0].split(":")
            tTiempo.horas += int(rtTIempo[0])
            tTiempo.minutos += int(rtTIempo[1])
        tTiempo._actualizar()
        return tTiempo

    def imprimir_tiempo(self):
        print(str(self.horas)+":"+str(self.minutos))

class fecha:
    dia = None
    mes = None
    anio = None
    def __init__(self,*arg):
        if len(arg) == 0:
            ffecha = input("Ingresa la fecha (DD-MM-AAAA) => ").split('-')
            self.dia = int(ffecha[0])
            self.mes = int(ffecha[1])
            self.anio = int(ffecha[2])
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

    def sumaFecha(self,*arg):
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


class persona:
    nombre = None
    apellidos = None
    genero = None
    curp = None
    tel_movil = None
    tel_casa = None
    __password = None
    def __init__(self,arg = None):
        # Ingreso completo
        if arg == True:
            self.nombre = input("Nombre(s) => ").split()
            self.apellidos = input("Apellidos => ").split()
            self.genero = input("Genero => ")
            self.curp = input("CURP => ")
            self.tel_movil = int(input("Telefono movil => "))
            self.tel_casa = int(input("Telefono de casa => "))
            self.password = int(input("Password (Solo numeros) => "))
        # Ingreso solo necesario
        elif arg == False or arg == None:
            self.nombre = input("Nombre(s) =>").split()
            self.apellidos = input("Apellitos => ").split()
            self.curp = input("CURP => ")
            self.password = int(input("Password (Solo numeros) => "))
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
        
class prestamo(fecha,tiempo,persona):
    dinero_prestado = float
    solicitud = int
    plazos = []
    def __init__(self,*arg):
        if len(arg) == 0:
            self.solicitud = input("Numero de solicitud => ")
            print("Fecha del prestamo")
            fecha.__init__(self)
            tiempo.__init__(self)
        elif len(arg) == 1 and isinstance(arg[0],int):
            self.solicitud = arg[0]
            print("Fecha del prestamo")
            fecha.__init__(self)
            tiempo.__init__(self)
        elif len(arg) == 3 and isinstance(arg[0],int) and isinstance(arg[1],str) and isinstance(arg[2],str):
            self.solicitud = arg[0]
            fecha.__init__(self,arg[1])
            tiempo.__init__(self,arg[2])
        if self.verificarFecha():
            print("".center(75,'-'))
            print("Desea ingresar datos completos o los necesarios del usuario")
            opt = int(input("1) Completos -- 2) Incompletos => "))
            print("".center(75,'-'))
            opt = True if opt == 1 else False
            persona.__init__(self,opt)
        else:
            print("Solo hay prestamos los primeros 20 dias del mes")

    def crearPrestamo(self,*arg):
        if len(arg) == 0:
            self.dinero_prestado = float(input("Ingrese el dinero que solicita => "))
        return self.dinero_prestado

    def verificarFecha(self) -> bool:
        return self.dia < 21
    
    def crearPlazos(self,*arg):
        tplazos = 0
        if len(arg) == 0:
            tplazos = int(input("Ingrese el numero de plazos => "))
        elif len(arg) == 1 and isinstance(arg[0],int):
            tplazos = arg[0]
        print("Plazos de pago".center(75,'-'))
        ffecha = fecha(self.dia,self.mes,self.anio)
        for x in range(tplazos):
            ffecha = ffecha.sumaFecha(30)
            self.plazos.append(ffecha)
        for x in self.plazos:
            x.imprimir_fecha()
    
class banco:
    __montoMaximo = 10000
    def verificarMonto(self,arg):
        return self.__montoMaximo >= arg
    def autorizarMonto(self,fFecha,tTiempo):
        tTiempo = tTiempo.sumaTiempo(1,0)
        fFecha = fFecha.sumaFecha(tTiempo.enviarDias())
        fFecha.imprimir_fecha()
        tTiempo.imprimir_tiempo()