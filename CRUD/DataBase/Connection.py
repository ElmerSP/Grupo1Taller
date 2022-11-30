import pymysql
import os

class Connection:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            port= 3307,
            password ='jhon',
            database = 'agenda'
        )
        self.cursor = self.connection.cursor()
    