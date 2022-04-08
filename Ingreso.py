import os
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def ingreso(correo, clave):
    if correo==" " or clave==" ":
        nombre=" "
        return nombre
    else:
        nombre=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT Nombre,Clave,rol FROM  Usuarios WHERE Correo=?"
        cursor_db.execute(sql, (correo,))
        consulta= cursor_db.fetchone()
        if consulta is not None:
                if consulta[1]==clave:
                    nombre=consulta
                    return nombre
                else : 
                    nombre=" "
                    return  nombre
        else:
            nombre=" "
            return nombre
