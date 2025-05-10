
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # ex: 'root'
        password="teste10",     # ex: '1234'
        database="registros"
    )