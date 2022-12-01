from DataBase.Connection import Connection
import os

class RegistroDB:
    def __init__(self):
        self._registro= Connection()
    
    def CodigoReunion(self):
        idGrupo=int(input("Ingrese ID del Grupo: "))
        idPersona=int(input("Ingrese ID del Persona: "))
        idReunion=int(input("Ingrese ID dela Reunion: "))
        sql="insert into grupo(idGrupo,idPersona,idReunion) values({},{},{})".format(idGrupo,idPersona,idReunion)
        self._registro.cursor.execute(sql)
        print("Ingresado correctamente ")
        self._registro.cursor.connection.commit()
        os.system('pause')
        os.system('cls')
    
    def InsertarEvento(self,idReunion,temaReunion,lugar,fecha,hora):
        sql = "insert into reunion (idReunion,temaReunion,lugar,fecha,hora) values({},'{}','{}','{}','{}')".format(idReunion,temaReunion,lugar,fecha,hora)
        self._registro.cursor.execute(sql)
        print("Ingresado correctamente ")
        self._registro.cursor.connection.commit()
        os.system('pause')
        os.system('cls')
        
    def InsertarPersona(self,idPersona,nombre,apellido,ci):
        sql=("insert into persona (idPersona,nombre,apellido,ci) values({},'{}','{}',{})".format(idPersona,nombre,apellido,ci))
        self._registro.cursor.execute(sql)
        print("Ingresado correctamente ")
        self._registro.cursor.connection.commit()
        os.system('pause')
        os.system('cls')