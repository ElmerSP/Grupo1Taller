from Menu import Menu
from read.mainread import MainRead
from delete.maindelete import MainDelete
class Main:
    def __init__(self):
        self.menus = Menu()
        self.mainread = MainRead()
        self.maindelete = MainDelete()
        
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
                self.maindelete.MenuEliminar()
            elif opcion == 0:
                print('gracias por usar el sistema...')