from Menu import Menu
from update.persona import Conector
from update.reunion import Reunion
import os
class MainUpdate:
    def __init__(self):
        self.menu = Menu() 
        self.persona = Conector()
        self.reunion = Reunion()
        
    def InicioMenu(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuUpdate()
            try:              
                opcion=int(input('Ingrese su opcion: '))
            except:
                print('deve ingresar un numero')
                input()
                os.system('cls')
            if opcion == 1:
                self.persona.cambiarNombre()
            if opcion == 2:
                self.persona.cambiarCi()
            if opcion == 3:
                self.reunion.cambiarTemaReunion()
            if opcion == 4:
                self.reunion.cambiarLugarReunion()
            if opcion == 5:
                self.reunion.cambiarFechaReunion()
            if opcion == 6:
                self.reunion.cambiarHoraReunion()
            elif opcion == 0:
                print('gracias por usar el sistema...')