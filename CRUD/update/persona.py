from DataBase.Connection import Connection
import os

class Conector:
    def __init__(self):
        self.coneccion = Connection()
        
    def cambiarNombre(self):
        nombre = input('Ingrese el nombre a remplazar: ')
        nuevoNombre = input('Ingrese el nuevo nombre: ')
        sql = "update Persona set nombre = '{}' where nombre = '{}'".format(nuevoNombre, nombre)
        self.coneccion.cursor.execute(sql)
        self.coneccion.connection.commit()
        print("Elemento actualizado \n")
        os.system('pause')
        os.system('cls')
        
    def cambiarCi(self):
        ci = input('Ingrese el CI a remplazar: ')
        nuevoCi = input('Ingrese el nuevo CI: ')
        sql = "update Persona set ci = '{}' where ci = '{}'".format(nuevoCi, ci)
        self.coneccion.cursor.execute(sql)
        self.coneccion.connection.commit()
        print("Elemento actualizado \n")
        os.system('pause')
        os.system('cls')
        