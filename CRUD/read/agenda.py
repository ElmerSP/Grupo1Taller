from DataBase.Connection import Connection
import os

class Agenda:
    def __init__(self):
        self.coneccion = Connection()
    
    def ConsultaAgenda(self):
        sql = "select * from reunion"
        self.coneccion.cursor.execute(sql)
        agenda = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("            Lista de Agenta")
        for i in agenda:
            print("Numero Identificador: ", i[0])
            print("Tema de la Reunion: ", i[1])
            print("Lugar: ", i[2])
            print("Fecha: ", i[3])
            print("Hora: ", i[4])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
    
    def consultaFecha(self):
        fecha = input("Ingerese la fecha: ")
        sql = "select * from reunion where fecha LIKE '%s'" %fecha 
        self.coneccion.cursor.execute(sql)
        agendafecha = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("        Lista de Agenta por Fecha")
        for i in agendafecha:
            print("Numero Identificador: ", i[0])
            print("Tema de la Reunion: ", i[1])
            print("Lugar: ", i[2])
            print("Fecha: ", i[3])
            print("Hora: ", i[4])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
    def consultaTema(self):
        tema = input("Por favor ingrese el tema: ")
        sql = "select * from reunion where TemaReunion LIKE '%s'" %tema
        self.coneccion.cursor.execute(sql)
        agendatema = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("        Lista de Agenta por Tema")
        for i in agendatema:
            print("Numero Identificador: ", i[0])
            print("Tema de la Reunion: ", i[1])
            print("Lugar: ", i[2])
            print("Fecha: ", i[3])
            print("Hora: ", i[4])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
