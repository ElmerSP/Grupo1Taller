from Menu import Menu
from read.mainread import MainRead
class Main:
    def __init__(self):
        self.menus = Menu()
        self.mainread = MainRead()
        
    def Inicio(self):
        opcion =-1
        while opcion!=0:
            self.menus.menuPrincipal()
            opcion= int(input('Ingrese su opcion por favor... '))
            if opcion == 1:
                self.funciones.Insertar()
            if opcion == 2:
                self.mainread.InicioMenu()
            if opcion == 3:
                self.funciones.Actualizar()
            if opcion == 4:
                self.funciones.Eliminar()
            elif opcion == 0:
                print('gracias por usar el sistema...')