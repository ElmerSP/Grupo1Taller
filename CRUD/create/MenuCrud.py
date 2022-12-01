from Menu import Menu
from create.ConexionBD import RegistroDB
from create.Funciones import Funciones
class MenuCrud:
    def __init__(self):
        self.registro= RegistroDB()
        self.registroFuncion=Funciones()
    def menuCrud(self):
        opcion =-1
        while opcion!=0:
            print('''
            ---->>>> Menu <<<<----
            [1] Registar Persona  [3] Registrar Grupo
            [2] Registrar Reunion [0] salir
            ''')
            
            opcion=int(input("Ingrese Opcion:  "))
            
            if opcion ==1:
                self.registroFuncion.RegistrarPersona()
            elif opcion ==2:
                self.registroFuncion.RegistroReunion()
            elif opcion ==3:
                self.registro.CodigoReunion()
        else:
            Menu()