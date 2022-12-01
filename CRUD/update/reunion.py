from DataBase.Connection import Connection
import os

class Reunion:
    def __init__(self):
        self.coneccion = Connection()
        
    def cambiarTemaReunion(self):
        temaReunion = input('Ingrese el tema de la reunion a remplazar: ')
        nuevoTema = input('Ingrese el tema para la reunion nombre: ')
        sql = "update Reunion set temaReunion = '{}' where temaReunion = '{}'".format(nuevoTema, temaReunion)
        self.coneccion.cursor.execute(sql)
        self.coneccion.connection.commit()
        print("Elemento actualizado \n")
        os.system('pause')
        os.system('cls')
        
    def cambiarLugarReunion(self):
        lugar = input('Ingrese el tema de la reunion a remplazar: ')
        nuevoLugar = input('Ingrese el nuevo tema para la reunion: ')
        sql = "update Reunion set lugar = '{}' where lugar = '{}'".format(nuevoLugar, lugar)
        self.coneccion.cursor.execute(sql)
        self.coneccion.connection.commit()
        print("Elemento actualizado \n")
        os.system('pause')
        os.system('cls')
        
    def cambiarFechaReunion(self):
        fecha = input('Ingrese la fecha a remplazar: ')
        nuevaFecha = input('Ingrese la nueva fecha: ')
        sql = "update Reunion set fecha = '{}' where fecha = '{}'".format(nuevaFecha, fecha)
        self.coneccion.cursor.execute(sql)
        self.coneccion.connection.commit()
        print("Elemento actualizado \n")
        os.system('pause')
        os.system('cls')
        
    def cambiarHoraReunion(self):
        hora = input('Ingrese la hora a remplazar: ')
        nuevaHora = input('Ingrese la nueva hora: ')
        sql = "update Reunion set hora = '{}' where hora = '{}'".format(nuevaHora, hora)
        self.coneccion.cursor.execute(sql)
        self.coneccion.connection.commit()
        print("Elemento actualizado \n")
        os.system('pause')
        os.system('cls')