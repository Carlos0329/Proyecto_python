import os
import sqlite3

from Registar import producto


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")


def Consulta_usuarios():
        usuarios=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT * FROM  Usuarios"
        cursor_db.execute(sql)
        usuarios=cursor_db.fetchall()
        if usuarios is not None:

            return usuarios
              
        else:
            usuarios=["Sin Datos registrados"]
            return usuarios

def Consulta_categoria():
        categorias=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT * FROM  Categoria"
        cursor_db.execute(sql)
        categorias=cursor_db.fetchall()
        if categorias is not None:

            return categorias
              
        else:
            categorias="Sin Datos registrados"
            return categorias
        
def Consulta_categoria_id(Id):
        categorias=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT * FROM  Categoria WHERE Id=?"
        cursor_db.execute(sql,(Id,))
        categorias=cursor_db.fetchall()
        if categorias is not None:

            return categorias
              
        else:
            categorias="Sin Datos registrados"
            return categorias

def Consulta_producto_id(Id):
        producto=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT * FROM  Producto WHERE Id=?"
        cursor_db.execute(sql,(Id,))
        producto=cursor_db.fetchall()
        if producto is not None:

            return producto
              
        else:
            producto="Sin Datos registrados"
            return producto


def Consulta_proveedor():
        proveedor=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT * FROM  proveedor"
        cursor_db.execute(sql)
        proveedores=cursor_db.fetchall()
        if proveedor is not None:

            return proveedores
              
        else:
            proveedores="Sin Datos registrados"
            return proveedor

def Consulta_producto():
        productos=[]
        #se conecta a la base de datos
        con_bd = sqlite3.connect('codeina.db')
        #cursor a la db
        cursor_db = con_bd.cursor()
        #consultass
        sql = "SELECT * FROM  producto"
        cursor_db.execute(sql)
        productos=cursor_db.fetchall()
        if productos is not None:

            return productos
              
        else:
            productos="Sin Datos registrados"
            return productos
