from DataBase.Connection import Connection
import os

class Conector:
    def __init__(self):
        self.coneccion = Connection()
    
    def ConsultaPersona(self):
        sql = "select * from persona"
        self.coneccion.cursor.execute(sql)
        personas = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("            Lista de Personas")
        for i in personas:
            print("Numero Identificador: ", i[0])
            print("Nombre: ", i[1])
            print("Apellido: ", i[2])
            print("CI: ", i[3])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
    def consultaAsistente(self):
        asistente = input("Por favor ingrese el nombre del asistente: ")
        sql = "select a.idreunion, p.nombre, a.TemaReunion, a.lugar, a.fecha, a.hora from persona p inner join grupo g on g.idpersona = p.idpersona inner join reunion a on a.idreunion = g.idreunion where p.nombre Like '%s'" %asistente
        self.coneccion.cursor.execute(sql)
        consultaasistente = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("            Lista de Personas")
        for i in consultaasistente:
            print("Numero Identificador: ", i[0])
            print("Nombre: ", i[1])
            print("Tema de la Reunion: ", i[2])
            print("Lugar: ", i[3])
            print("Fecha: ", i[4])
            print("Hora: ", i[5])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')