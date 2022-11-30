from create.Persona import Persona
from create.Agenda import Agenda
from create.RegistroBD import RegistroDB
from DataBase.Connection import Connection

class Funciones:
    
    def __init__(self):
        self.base = RegistroDB()
        self.listapersona=[]
        self.listaAgenda=[]

    def RegistrarPersona(self):
        '''self.base.CodigoReunion()'''
        idReunion=int(input("Ingrese Id Reunion: "))
        temaReunion= input('Tema sobre la reunion: ')
        lugar= input('Ingrese lugar: ')
        fecha= input("ingrese fechaÑ ")
        hora=input('ingrese hora: ')
        if idReunion!='' and temaReunion != '' and lugar != '' and fecha != '' and hora !='':
            agenda=Agenda(idReunion,temaReunion,lugar,fecha,hora)
            self.listaAgenda.append(agenda)
            for i in self.listaAgenda:
                idReunion=i.get_idReunion()
                temaReunion=i.get_temaReunion()
                lugar=i.get_lugar()
                fecha=i.get_fecha()
                hora=i.get_hora()
                self.base.InsertarEvento(idReunion,temaReunion,lugar,fecha,hora)
            self.listaAgenda.clear()
        print("*"*50)
        contador=int(input("Cuantas personas desea Agregar ala Reunion: "))
        for i in range(contador):
            print("*"*50)
            print("Por favor ingrese datos de la personas: ")
            print("*"*50)
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
            else:
                print("datos inncorrectos")
            print(">>>>Registro exitoso<<<<")
        self.base.CodigoReunion()
        

        