import pymysql
import os

class Connection:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password ='12345',
            database = 'agenda'
        )
        self.cursor = self.connection.cursor()
    def InsertarEvento(self,idAgenda,idPersona,temaReunion,lugar,fecha,hora):
        sql = "insert into reunion (idAgenda,idPersona,temaReunion,lugar,fecha,hora) values({},{},'{}','{}','{}','{}')".format(idAgenda,idPersona,temaReunion,lugar,fecha,hora)
        self.cursor.execute(sql)
        print("Ingresado correctamente ")
        self.cursor.connection.commit()
        os.system('pause')
        os.system('cls')
        
    def InsertarPersona(self,idPersona,nombre,apellido,ci):
        sql=("insert into persona (idPersona,nombre,apellido,ci) values({},'{}','{}',{})".format(idPersona,nombre,apellido,ci))
        self.cursor.execute(sql)
        self.cursor.connection.commit()
        os.system('pause')
        os.system('cls')