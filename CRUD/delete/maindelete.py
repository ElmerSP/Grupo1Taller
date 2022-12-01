from Menu import Menu
from delete.reunion import EliminarReunion
from delete.grupo import EliminarGrupo
from delete.persona import EliminarPersona
import os
class MainDelete:
    def __init__(self):
        self.menu = Menu() 
        self.eliminar = EliminarReunion()
        self.eliminargrupo = EliminarGrupo()
        self.eliminarpersona = EliminarPersona()
        
    def MenuEliminar(self):
        opcion =-1
        while opcion!=0:
            self.menu.menuDelete()
            try:              
                opcion=int(input('Ingrese su opcion: '))
            except:
                print('deve ingresar un numero')
                input()
                os.system('cls')
            if opcion == 1:
                self.eliminargrupo.eliminargrupo()
            elif opcion == 2:
                self.eliminarpersona.eliminapersona()
            elif opcion == 3:
                self.eliminar.eliminarreunion()
            elif opcion == 0:
                print('gracias por usar el sistema...')