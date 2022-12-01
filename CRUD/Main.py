from Menu import Menu
from read.mainread import MainRead
from delete.maindelete import MainDelete
from create.MenuCreate import MenuCreate
import os
class Main:
    def __init__(self):
        self.menuCreate=MenuCreate()
        self.menu = Menu()
        self.mainread = MainRead()
        self.maindelete = MainDelete()
          
    def Inicio(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuPrincipal()
            try:              
                opcion=int(input('Ingrese su opcion: '))
            except:
                print('deve ingresar un numero')
                input()
                os.system('cls')
            if opcion == 1:
                self.menuCreate.inicioCreate()
            if opcion == 2:
                self.mainread.InicioMenu()
            if opcion == 3:
                pass
            if opcion == 4:
                self.maindelete.MenuEliminar()
            elif opcion == 0:
                print('gracias por usar el sistema...')