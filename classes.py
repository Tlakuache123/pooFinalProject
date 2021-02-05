from math import ceil
import os
import csv
import pandas

columnas = ['Dia','Hora','Nombre1','Nombres2','Apellido1','Apellido2','Genero','CURP','tel_movil','tel_casa','password','prestamos']
default_path = "prestamo.csv"

def empty_file(path:str):
    if os.path.getsize(path) == 0:
        return True
    else:
        return False

def search(path:str,name:str,apellido:str):
    with open(path,'r') as f:
        csvread = csv.reader(f)
        for row in csvread:
            if row[2].lower() == name.lower() and row[4].lower() == apellido.lower():
                return row

def checkPassword(rowObj):
    password = int(rowObj[10])
    Upass = int(input("Constraseña => "))
    return password == Upass

class tiempo:
    minutos = 0
    horas = 0
    dias = 0
    def __init__(self,*arg):
        if len(arg) == 0:
            htiempo = input("Ingrese el tiempo (HH:MM) => ").split(':')
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
    
    def recargarTiempo(self,*arg):
        if len(arg) == 0:
            htiempo = input("Ingrese el tiempo (HH:MM) => ").split(':')
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

    def recargarFecha(self,*arg):
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
    def __init__(self,*arg):
        # Ingreso completo
        if len(arg) == 1 and arg[0] == True:
            self.nombre = input("Nombre(s) => ").split()
            self.apellidos = input("Apellidos => ").split()
            self.genero = input("Genero => ")
            self.curp = input("CURP => ")
            self.tel_movil = input("Telefono movil => ")
            self.tel_casa = input("Telefono de casa => ")
            self.password = int(input("Password (Solo numeros) => "))
        # Ingreso solo necesario
        elif len(arg) == 1 and arg[0] == False:
            self.nombre = input("Nombre(s) =>").split()
            self.apellidos = input("Apellitos => ").split()
            self.curp = input("CURP => ")
            self.password = int(input("Password (Solo numeros) => "))
        elif len(arg) == 7:
            self.nombre = arg[0]
            self.apellidos = arg[1]
            self.genero = arg[2]
            self.curp = arg[3]
            self.tel_movil = arg[4]
            self.tel_casa = arg[5]
            self.password = int(arg[6])
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
        
class prestamo(fecha,tiempo,persona):
    guardar = False
    _interes = 0.15
    num_prestamo = 0
    dinero_prestado = 0.0
    dinero_pagar = 0.0
    pagos_plazo = 0.0
    solicitud = 0
    plazos = []
    def __init__(self,*arg):
        if len(arg) == 0:
            fecha.__init__(self)
            tiempo.__init__(self)
            if self.verificarFecha():
                print("".center(75,'-'))
                print("Desea ingresar datos completos o los necesarios del usuario")
                opt = int(input("1) Completos -- 2) Incompletos => "))
                print("".center(75,'-'))
                opt = True if opt == 1 else False
                persona.__init__(self,opt)
        elif len(arg) == 2 and isinstance(arg[0],str) and isinstance(arg[1],str):
            fecha.__init__(self,arg[0])
            tiempo.__init__(self,arg[1])
            if self.verificarFecha():
                print("".center(75,'-'))
                print("Desea ingresar datos completos o los necesarios del usuario")
                opt = int(input("1) Completos -- 2) Incompletos => "))
                print("".center(75,'-'))
                opt = True if opt == 1 else False
                persona.__init__(self,opt)
        elif len(arg) == 10:
            fecha.__init__(self,arg[0])
            tiempo.__init__(self,arg[1])
            persona.__init__(self,arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],arg[8])
            self.num_prestamo = int(arg[9])

    def __del__(self):
        if self.guardar:
            ffecha = str(self.dia) + "-" + str(self.mes) + "-" + str(self.anio)
            ttiempo = str(self.horas) + ":" + str(self.minutos)

            if len(self.nombre) == 2:
                nnombre = [self.nombre[0],self.nombre[1]]
            else:
                nnombre = [self.nombre[0],""]
            
            if len(self.apellidos) == 2:
                aapellido = [self.apellidos[0],self.apellidos[1]]
            else:
                aapellido = [self.apellidos[0],""]

            if search(default_path,self.nombre[0],self.apellidos[0]) == None:
                with open(default_path,'a') as f:
                    csvWrite = csv.writer(f)
                    csvWrite.writerow([ffecha,ttiempo,nnombre[0],nnombre[1],aapellido[0],aapellido[1],self.genero,self.curp,self.tel_movil,self.tel_movil,self.password,self.num_prestamo])
            else:
                df = pandas.read_csv(default_path)
                df.loc[df["CURP"]==self.curp, "prestamos"] = self.num_prestamo
                df.loc[df["CURP"]==self.curp, "Dia"] = ffecha
                df.loc[df["CURP"]==self.curp, "Hora"] = ttiempo
                df.to_csv(default_path,index=False)

    def crearPrestamo(self,*arg):
        self.num_prestamo += 1
        self.dinero_prestado = float(input("Ingrese el dinero que solicita => "))
        self.dinero_pagar = ceil(self.dinero_prestado + (self.dinero_prestado * self._interes))

    def verificarFecha(self) -> bool:
        return self.dia < 21
    
    def crearPlazos(self,*arg):
        tplazos = 0
        if len(arg) == 0:
            tplazos = int(input("Ingrese el numero de plazos (Maximo 6) => "))
        elif len(arg) == 1 and isinstance(arg[0],int):
            tplazos = arg[0]
        while(tplazos > 6 or tplazos < 0):
            print("*ERROR* Ingrese un numero entre 1 y 6 *ERROR*")
            tplazos = int(input("Ingrese el numero de plazos (Maximo 6) => "))
        ffecha = fecha(self.dia,self.mes,self.anio)
        for x in range(tplazos):
            ffecha = ffecha.sumaFecha(30)
            self.plazos.append(ffecha)
        self.pagos_plazo = ceil(self.dinero_pagar/tplazos)
        self.pagos_plazo = round(self.pagos_plazo,2)
    
    def imprimirPrestamo(self):
        print("DATOS DEL ULTIMO PRESTAMO".center(75,'-'))
        self.imprimir_usuario()
        print("Hora de prestamo".center(75,'-'))
        print(("Fecha:" + str(self.dia) + "-" + str(self.mes) + "-" + str(self.anio)).center(38),end="")
        print(("Hora: " +str(self.horas) + ":" + str(self.minutos)).center(37))
        print("Informacion del prestamo".center(75,'-'))
        print("Num. Prestamo: " + str(self.num_prestamo).center(50))
        print("Prestamo: " + ("$" + str(self.dinero_prestado)).center(50))
        print("Pago total: " + ("$" + str(self.dinero_pagar)).center(50))
        print("Plazos de pago".center(75,'-'))
        i = 1
        for x in self.plazos:
            print((str(i) + "- Fecha: " + str(x.dia) + "-" + str(x.mes) + "-" + str(x.anio)).ljust(37),end="")
            print(("Pago: $" + str(self.pagos_plazo)).center(38))
            i += 1
    
class banco:
    __montoMaximo = 10000
    def verificarMonto(self,arg):
        return self.__montoMaximo >= arg
    def autorizarMonto(self,fFecha,tTiempo):
        tTiempo = tTiempo.sumaTiempo(1,0)
        fFecha = fFecha.sumaFecha(tTiempo.enviarDias())
        fFecha.imprimir_fecha()
        tTiempo.imprimir_tiempo()