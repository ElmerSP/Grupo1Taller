from persona import Persona
from agenda import Agenda
from DataBase.Connection import Connection

class Funciones:
    
    def __init__(self):
        self.base = Connection()
        self.listapersona=[]
        self.listaAgenda=[]

    def RegistrarPersona(self):
        idPersona=int(input("Ingrese ID de la persona: "))
        nombre=input("Ingrese Nombre: ")
        apellido=input("ingrese Apellido: ")
        ci=int(input("ingrese ci: "))
        if idPersona !='' and nombre != '' and apellido!='' and ci!='':
            persona=Persona(int(idPersona),nombre,apellido,int(ci))
            self.listapersona.append(persona)
            for i in self.listapersona:
                idPersona=i.get_idPersona()  
                nombre=i.get_nombre()
                apellido=i.get_apellido()
                ci=i.get_ci()
                self.base.InsertarPersona(idPersona,nombre,apellido,ci)
            self.listapersona.clear()
            
        print("*"*50)
        print("Por favor ingrese datos dela agenda: ")
        print("*"*50)
        
        idAgenda=int(input("Ingrese Id Agenda: "))
        idPersona = int(input('Ingrese id Persona: '))
        temaReunion= input('Tema sobre la reunion: ')
        lugar= input('Ingrese lugar: ')
        fecha= input("ingrese fecha")
        hora=input('ingrese hora: ')
        if idAgenda!='' and idPersona !=''and temaReunion != '' and lugar != '' and fecha != '' and hora !='':
            agenda=Agenda(idAgenda,idPersona,temaReunion,lugar,fecha,hora)
            self.listaAgenda.append(agenda)
            for i in self.listaAgenda:
                idAgenda=i.get_idAgenda()
                idPersona=i.get_idPersona()
                temaReunion=i.get_temaReunion()
                lugar=i.get_lugar()
                fecha=i.get_fecha()
                hora=i.get_hora()
                self.base.InsertarEvento(idAgenda,idPersona,temaReunion,lugar,fecha,hora)
            self.listaAgenda.clear()
            
        print(">>>>Registro exitoso<<<<")
        