from read.MenuRead import menuread
from read.persona import Conector
from read.agenda import Agenda
class MainRead:
    def __init__(self):
        self.menu2 = menuread() 
        self.persona = Conector()
        self.agenda = Agenda()
        
    def InicioMenu(self):
        opcion =-1
        while opcion!=0:
            self.menu2.menu()
            opcion= int(input('Ingrese su opcion por favor... '))
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
            # if opcion == 4:
            #     self.funciones.Eliminar()
            elif opcion == 0:
                print('gracias por usar el sistema...')