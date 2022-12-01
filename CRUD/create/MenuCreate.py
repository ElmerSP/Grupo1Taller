from Menu import Menu
from create.ConexionBD import RegistroDB
from create.Funciones import Funciones
import os
class MenuCreate:
    def __init__(self):
        self.menu = Menu()
        self.registro= RegistroDB()
        self.registroFuncion=Funciones()
    def inicioCreate(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuCrear()
            try:              
                opcion=int(input("Ingrese una opcion: "))
            except:
                print('deve ingresar un numero')
                input()
                os.system('cls')
            if opcion ==1:
                self.registroFuncion.RegistrarPersona()
            if opcion ==2:
                self.registroFuncion.RegistroReunion()
            if opcion ==3:
                self.registro.CodigoReunion()
            elif opcion == 0:
                print('gracias por usar el sistema...')
        