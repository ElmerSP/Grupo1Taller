from DataBase.Connection import Connection
import os

class Agenda:
    def __init__(self):
        self.coneccion = Connection()
    
    def ConsultaAgenda(self):
        sql = "select * from agenda"
        self.coneccion.cursor.execute(sql)
        agenda = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("            Lista de Agenta")
        for i in agenda:
            print("Numero Identificador: ", i[0])
            print("Identificador Persona: ", i[1])
            print("Tema de la Reunion: ", i[2])
            print("Lugar: ", i[3])
            print("Fecha: ", i[4])
            print("Hora: ", i[5])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
    
    def consultaFecha(self):
        fecha = input("Ingerese la fecha: ")
        sql = "select * from Agenda where fecha LIKE '%s'" %fecha 
        self.coneccion.cursor.execute(sql)
        agendafecha = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("        Lista de Agenta por Fecha")
        for i in agendafecha:
            print("Numero Identificador: ", i[0])
            print("Identificador Persona: ", i[1])
            print("Tema de la Reunion: ", i[2])
            print("Lugar: ", i[3])
            print("Fecha: ", i[4])
            print("Hora: ", i[5])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
    def consultaTema(self):
        tema = input("Por favor ingrese el tema: ")
        sql = "select * from agenda where TemaReunion LIKE '%s'" %tema
        self.coneccion.cursor.execute(sql)
        agendatema = self.coneccion.cursor.fetchall()
        print("#############################################")
        print("        Lista de Agenta por Tema")
        for i in agendatema:
            print("Numero Identificador: ", i[0])
            print("Identificador Persona: ", i[1])
            print("Tema de la Reunion: ", i[2])
            print("Lugar: ", i[3])
            print("Fecha: ", i[4])
            print("Hora: ", i[5])
            print("-------------------------------------")
        os.system('pause')
        os.system('cls')
