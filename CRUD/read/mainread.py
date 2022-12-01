from Menu import Menu
from read.persona import Conector
from read.agenda import Agenda
import os
class MainRead:
    def __init__(self):
        self.menu = Menu() 
        self.persona = Conector()
        self.agenda = Agenda()
        
    def InicioMenu(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuRead()
            try:              
                opcion=int(input('Ingrese su opcion: '))
            except:
                print('deve ingresar un numero')
                input()
                os.system('cls')
            if opcion == 1:
                self.agenda.consultaFecha()
            if opcion == 2:
                self.persona.consultaAsistente()
            if opcion == 3:
                self.agenda.consultaTema()
            if opcion == 4:
                self.persona.ConsultaPersona()
            if opcion == 5:
                self.agenda.ConsultaAgenda()
            elif opcion == 0:
                print('gracias por usar el sistema...')