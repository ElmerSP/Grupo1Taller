from Menu import Menu
from CRUD.create.Funciones import Funciones
import os

class Main:
    def __init__(self):
        self.menu = Menu()
        self.funcion=Funciones()
    def Inicio(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuPrincipal()
            try:              
                opcion=int(input(">> "))
            except:
                print('deve ingresar un numero')
                input()
                os.system('cls')
            if opcion == 1:
                self.funcion.RegistrarPersona()
            if opcion == 2:
                pass
            if opcion == 3:
                pass
            if opcion == 4:
                pass
            elif opcion == 0:
                print('gracias...')