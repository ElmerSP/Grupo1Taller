from delete.MenuDelete import menudelete
from delete.reunion import EliminarReunion
from delete.grupo import EliminarGrupo
from delete.persona import EliminarPersona
class MainDelete:
    def __init__(self):
        self.menueliminar = menudelete() 
        self.eliminar = EliminarReunion()
        self.eliminargrupo = EliminarGrupo()
        self.eliminarpersona = EliminarPersona()
        
    def MenuEliminar(self):
        opcion =-1
        while opcion!=0:
            self.menueliminar.menu()
            opcion= int(input('Ingrese su opcion por favor... '))
            if opcion == 1:
                self.eliminargrupo.eliminargrupo()
            elif opcion == 2:
                self.eliminarpersona.eliminapersona()
            elif opcion == 3:
                self.eliminar.eliminarreunion()
            elif opcion == 0:
                print('gracias por usar el sistema...')