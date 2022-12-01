from DataBase.Connection import Connection
import os

class EliminarGrupo:
    def __init__(self):
        self.coneccion = Connection()

    def eliminargrupo(self):
            numeroID = int(input('Ingrese el numero de ID que quiere eliminar: '))
            sql = "delete from grupo where idgrupo = '{}'".format(numeroID)
            self.coneccion.cursor.execute(sql)
            self.coneccion.connection.commit()
            print("Elemento eliminado \n")
            os.system('pause')
            os.system('cls')