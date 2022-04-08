from Registar import *
from Consultas import *
from Ingreso import ingreso
from Delete import *
from Actualizar import *
from flask import Flask
from flask import Flask, render_template, request, session, redirect, url_for

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "codeina.db")

app = Flask(__name__)
#con esta llave firmamos las cookies
app.secret_key = '54SF4GHAFHGAS4' 

#RUTA INDEX
@app.route('/')
def index():
    return render_template('index.html')

#RUTA FORMULARIO DE INGRESO
@app.route('/interfazingreso')
def interfaz_ingreso():
    return render_template('Ingreso.html')

#ACCION DE INGRESO
@app.route('/ingreso', methods=['POST'])
def ingreso_def():
    
    correo = request.form.get("correo")
    clave = request.form.get("clave")
    nombre=ingreso(correo,clave)
    session["user"]=correo
    if nombre!=" ":
        if nombre[2]=="Administrador":
            return render_template('Principal.html',nombre=nombre[0])
        elif nombre[2]=="Cajero":
            return render_template('P_vendedor.html',nombre=nombre[0])
        elif nombre[2]=="Bodeguero":
            return render_template('P_bodeguero.html',nombre=nombre[0])
    return redirect('/interfazingreso')

#RUTA FORMULARIO USUARIO
@app.route('/interfazusuarios')
def interfaz_usuarios():
    if "user" in session:
        usuarios=Consulta_usuarios()
        return render_template('Usuarios.html',usuarios=usuarios)
    return redirect('/')

#ACCION DE REGISTRO USUARIO
@app.route('/usuario', methods=['POST'])
def registro_usuario():
    if "user" in session:
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        correo = request.form.get("correo")
        clave = request.form.get("clave")
        rol = int(request.form.get("rol"))
        if rol==1:
            rol="Administrador"
        elif rol==2:
            rol="Cajero"
        elif rol==3:
            rol="Bodeguero"
        usuario=registrar(nombre,apellido,correo,clave,rol)
        if usuario:
            return redirect('/interfazusuarios')
        else:
            return redirect('/interfazprincipal')
    return redirect('/')

#ACCION ELIMINAR USUARIO
@app.route('/eliminar_usuario', methods=["POST"])
def eliminar_usuario():
    if "user" in session:
        id=request.form.get("id")
        resultado=delete_usuario(id)
        if resultado:
            return redirect("/interfazusuarios")
    return redirect('/')

#RUTA FORMULARIO PRODUCTO
@app.route('/interfazproductos')
def interfaz_productos():
    if "user" in session:
        opcionesCategoria=[]#lista categorias vacia
        opcionesProveedores=[]
        categorias=Consulta_categoria()
        proveedores=Consulta_proveedor()
        for categoria in categorias:
            opcionesCategoria.append(categoria[1])
        for proveedor in proveedores:
            opcionesProveedores.append(proveedor[1])
        productos=Consulta_producto()
        return render_template('Productos.html',productos=productos,categorias=opcionesCategoria,proveedores=opcionesProveedores)
    return redirect('/')
#ACCION FORMULARIO PRODUCTO
@app.route('/producto', methods=['POST'])
def registro_producto():
    if "user" in session:
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        cantidad = request.form.get("cantidad")
        precio_compra = request.form.get("precio_compra")
        precio_venta = request.form.get("precio_venta")
        categoria= request.form.get("categoria")
        proveedor= request.form.get("proveedor")
        a=producto(nombre,descripcion,cantidad,precio_compra,precio_venta,categoria,proveedor)
        if a:
            return redirect('/interfazproductos')
        else:
            return redirect('/interfazprincipal')
    return redirect('/')
#ACCION ELIMINAR PRODUCTO
@app.route('/eliminar_producto', methods=["POST"])
def eliminar_producto():
    if "user" in session:
        Id=request.form.get("Id")
        resultado=delete_producto(Id)
        if resultado:
            return redirect("/interfazproductos")
    return redirect('/')
#RUTA FORMULARIO CATEGORIA
@app.route('/interfazcategorias')
def interfaz_categorias():
    if "user" in session:
        categorias=Consulta_categoria()
        return render_template('Categorias.html', categorias=categorias)
    return redirect('/')
#ACCION REGISTRO CATEGORIA
@app.route('/categoria', methods=['POST'])
def registro_categoria():
    if "user" in session:
        nombre = request.form.get("nombre")
        a=categoria(nombre)
        if a:
            return redirect("/interfazcategorias")
        else:
            return render_template('Principal.html')
    return redirect('/')

#ACCION ELIMINAR CATEGORIA
@app.route('/eliminar_categoria', methods=["POST"])
def eliminar_categoria():
    if "user" in session:
        Id=request.form.get("Id")
        resultado=delete_categoria(Id)
        if resultado:
            return redirect("/interfazcategorias")
    return redirect('/')
#RUTA FORMULARIO PROVEEDOR
@app.route('/interfazproveedor')
def interfaz_proveedor():
    if "user" in session:
        proveedores=Consulta_proveedor()
        return render_template('Proveedores.html', proveedores=proveedores)
    return redirect('/')
#ACCION REGISTRO PROVEEDOR
@app.route('/proveedor', methods=['POST'])
def registro_proveedor():
    if "user" in session:
        nombre = request.form.get("nombre")
        telefono = request.form.get("telefono")
        direccion = request.form.get("direccion")
        a=proveedor(nombre,telefono,direccion)
        if a:
            return render_template('Proveedores.html')
        else:
            return render_template('Principal.html')
    return redirect('/')
#ACCION ELIMINAR PROVEEDOR
@app.route('/eliminar_proveedor', methods=["POST"])
def eliminar_proveedor():
    if "user" in session:
        Id=request.form.get("Id")
        resultado=delete_proveedor(Id)
        if resultado:
            return redirect("/interfazproveedor")
    return redirect('/')
#RUTA PANEL PRINCIPAL
@app.route('/interfazprincipal')
def interfaz_principal():
    if "user" in session:
        usuarios=Consulta_usuarios()
        print(len(usuarios))
        return render_template('Principal.html')
    return redirect('/')

#CIERRE
@app.route('/cerrar', methods=['GET'])
def cerrar():
    if "user" in session:
        session.pop("user")
        return redirect('/')
    else: 
        return redirect('/interfazingreso')


app.run(debug = False, port=5000)