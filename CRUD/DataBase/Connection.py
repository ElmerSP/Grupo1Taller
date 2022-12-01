import pymysql

class Connection:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            port= 3306,
            password ='12345',
            database = 'agenda'
        )
        self.cursor = self.connection.cursor()
      