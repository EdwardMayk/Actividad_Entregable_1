import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

import pymysql

def Conexion(query,interruptor):
    conn=pymysql.connect(host="localhost",
                         user="root",
                         password="root1",
                         database="tornillo")
    cursor=conn.cursor()
    cursor.execute(query)
    
    if interruptor=="prendido":
        conn.commit()
    return cursor
    conn.close()

def getCliente(codigo):
    query="SELECT*FROM clientes WHERE codigo="+str(codigo)
    a=Conexion(query, "apagado")
    b=a.fetchone()
    return b

def getProducto(codigo):
    query="SELECT*FROM productos WHERE codigo="+str(codigo)
    a=Conexion(query, "apagado")
    b=a.fetchone()
    return b




#==========================
def agregar():
    #obtener los valores a insertar
    dni = txtDNI.get()
    nombre = txtNombres.get()
    apellido = txtApellidos.get()
    direccion = txtDireccion.get()
    telefono = txtTelefono.get()

    if (dni == "" or nombre == "" or apellido == "" or direccion =="" or telefono ==""):
        MessageBox.showinfo("Insertar Registro","Todos los datos son requeridos")
    else:
        #Realizar la conexion a la BD
        con = mysql.connect(host="localhost",user="root",password="root1",database="tornillo")

        #Crear cursor para ejecutar comando SQL
        cursor = con.cursor()

        #realizar la instuccion SQL
        cursor.execute("insert into clientes (dni,nombres,apellidos,direccion,telefono) values('" + dni + "','" + apellido + "','" + nombre + "','" + direccion + "'," + str(telefono) + ")")
        cursor.execute("commit")

        #Actualizar treeview
        #mostrar()
        
        #Limpiar textos
        txtDNI.delete(0, 'end')
        txtNombres.delete(0, 'end')
        txtApellidos.delete(0, 'end')
        txtDireccion.delete(0, 'end')
        txtTelefono.delete(0, 'end')

        #Cerrar conexion
        con.close()

def mostrar():
    if (txtCodigo.get() == ""):
        MessageBox.showinfo("Leer Registro","Debe ingresar el codigo del lugar para leer los datos")
    else:
        #Conexion
        con = mysql.connect(host="localhost",user="root",password="root1",database="tornillo")

        #Crear cursor para ejecutar comando SQL
        cursor = con.cursor()
        cursor.execute("select * from clientes where codigo='" + txtCodigo.get() + "'")

        #Obtener los registros en una variable
        rows = cursor.fetchall()

        #
        txtDNI.delete(0, 'end')
        txtNombres.delete(0, 'end')
        txtApellidos.delete(0, 'end')
        txtDireccion.delete(0, 'end')
        txtTelefono.delete(0, 'end')
        
        for row in rows:
            txtDNI.insert(0, row[1])
            txtNombres.insert(0, row[2])
            txtApellidos.insert(0, row[3])
            txtDireccion.insert(0, row[4])
            txtTelefono.insert(0, row[5])

        #Cerrar conexion
        con.close()



def verProd():

    for tupla in lista:
        cod=tupla[0].get()
        tupla2=getProducto(cod)
        for j in range (1,4):
            tupla[j].insert(0,tupla2[j])
        
#def productos(txtCodProd):
    
            


"""
    
def productos():
    if (txtCodProd.get() == ""):
        MessageBox.showinfo("Leer Registro","Debe ingresar el codigo del lugar para leer los datos")
    else:
        #Conexion
        con = mysql.connect(host="localhost",user="root",password="root1",database="tornillo")

        #Crear cursor para ejecutar comando SQL
        cursor = con.cursor()
        cursor.execute("select * from productos where codigo='" + txtCodProd.get() + "'")

        #Obtener los registros en una variable
        rows = cursor.fetchall()

        #
        txtDescripcion.delete(0, 'end')
        txtUnidad.delete(0, 'end')
        txtPrecio.delete(0, 'end')
        #txtDireccion.delete(0, 'end')
        #txtTelefono.delete(0, 'end')
        
        for row in rows:
            txtDescripcion.insert(0, row[1])
            txtUnidad.insert(0, row[2])
            txtPrecio.insert(0, row[3])
            #txtDireccion.insert(0, row[4])
            #txtTelefono.insert(0, row[5])

        #Cerrar conexion
        con.close()

"""

def calcular():
        valor1=txtCantidad.get()
        valor2=txtCantidad1.get()
        valor3=txtCantidad2.get()
        valor4=txtPrecio.get()
        valor5=txtPrecio1.get()
        valor6=txtPrecio2.get()
        
        tot1=float(valor1) * float(valor4)
        tot2=float(valor2) * float(valor5)
        tot3=float(valor3) * float(valor6)
        tot4= tot1 + tot2 + tot3
        totround1=round(tot1,3)
        totround2=round(tot2,3)
        totround3=round(tot3,3)
        totround4=round(tot4,3)
        
        txtSubtotal.delete(0, 'end')
        txtSubtotal1.delete(0, 'end')
        txtSubtotal2.delete(0, 'end')
        txtTotal.delete(0, 'end')
        
        txtSubtotal.insert(0,totround1)
        txtSubtotal1.insert(0,totround2)
        txtSubtotal2.insert(0,totround3)
        txtTotal.insert(0,totround4)
        
        
            
        
    


def Limpiar():
        txtCodigo.delete(0, 'end')
        txtDNI.delete(0, 'end')
        txtNombres.delete(0, 'end')
        txtApellidos.delete(0, 'end')
        txtDireccion.delete(0, 'end')
        txtTelefono.delete(0, 'end')
        #Productos
        txtCodProd.delete(0, 'end')
        txtCodProd1.delete(0, 'end')
        txtCodProd2.delete(0, 'end')
        txtDescripcion.delete(0, 'end')
        txtDescripcion1.delete(0, 'end')
        txtDescripcion2.delete(0, 'end')
        txtUnidad.delete(0, 'end')
        txtUnidad1.delete(0, 'end')
        txtUnidad2.delete(0, 'end')
        txtCantidad.delete(0, 'end')
        txtCantidad1.delete(0, 'end')
        txtCantidad2.delete(0, 'end')
        txtPrecio.delete(0, 'end')
        txtPrecio1.delete(0, 'end')
        txtPrecio2.delete(0, 'end')
        txtSubtotal.delete(0, 'end')
        txtSubtotal1.delete(0, 'end')
        txtSubtotal2.delete(0, 'end')
        txtTotal.delete(0, 'end')
        

ven = Tk()
ven.title("Registro")

ven.geometry("600x500")
ven.config(bg="light gray")

ven.resizable(False, False)
"""
#Variables lo que podiblemente haremos más adelante
DNI = StringVar()
Apellidos = StringVar()
Nombres=StringVar()
Direccion=StringVar()
Telefono=StringVar()
"""
#Lbl
lbltitulo=Label(ven,text="Ferreteria 'El Tornillo Feliz'",font=("calibri",18,"bold"))
lbltitulo.place(x=180,y=10)
lbltitulo.config(bg="light gray")

lbldni=Label(ven,text="DNI",font=("calibri",14))
lbldni.place(x=60,y=60)
lbldni.config(bg="light gray")

lblcodigo=Label(ven,text="Codigo.Cliente",font=("calibri",14))
lblcodigo.place(x=300,y=60)
lblcodigo.config(bg="light gray")

lblApe=Label(ven,text="Apellidos",font=("calibri",14))
lblApe.place(x=50,y=100)
lblApe.config(bg="light gray")

lblNom=Label(ven,text="Nombres",font=("calibri",14))
lblNom.place(x=300,y=100)
lblNom.config(bg="light gray")

lblDir=Label(ven,text="Dirección",font=("calibri",14))
lblDir.place(x=40,y=140)
lblDir.config(bg="light gray")

lblTel=Label(ven,text="Teléfono",font=("Calibri",14))
lblTel.place(x=40,y=180)
lblTel.config(bg="light gray")

lblCodPro=Label(ven,text="Cod_Prod",font=("Calibri",13))
lblCodPro.place(x=40,y=270)
lblCodPro.config(bg="light gray")

lblDesc=Label(ven,text="Descripción",font=("calibri",13))
lblDesc.place(x=130,y=270)
lblDesc.config(bg="light gray")

lblUni=Label(ven,text="Unidad",font=("calibri",13))
lblUni.place(x=230,y=270)
lblUni.config(bg="light gray")

lblCant=Label(ven,text="Cantidad",font=("calibri",13))
lblCant.place(x=320,y=270)
lblCant.config(bg="light gray")

lblPrec=Label(ven,text="Precio",font=("calibri",13))
lblPrec.place(x=415,y=270)
lblPrec.config(bg="light gray")

lblSubT=Label(ven,text="Subtotal",font=("calibri",13))
lblSubT.place(x=490,y=270)
lblSubT.config(bg="light gray")

lblTot=Label(ven,text="Total",font=("calibri",12))
lblTot.place(x=470,y=440)
lblTot.config(bg="light gray")
#Cajas de texto
txtDNI=Entry(ven,font=("calibri",14,),width=15)
txtDNI.place(x=130,y=60)

txtCodigo=Entry(ven,font=("calibri",14,),width=10)
txtCodigo.place(x=430,y=60)

txtApellidos=Entry(ven,font=("calibri",14,),width=15)
txtApellidos.place(x=130,y=100)

txtNombres=Entry(ven,font=("calibri",14,),width=17)
txtNombres.place(x=385,y=100)

txtDireccion=Entry(ven,font=("calibri",14,),width=36)
txtDireccion.place(x=140,y=140)

txtTelefono=Entry(ven,font=("calibri",14,),width=36)
txtTelefono.place(x=140,y=180)

txtCodProd=Entry(ven,font=("calibri",13,),width=8)#state=DISABLED para que no se pueda escribir en las cajas
txtCodProd.place(x=40,y=310)

txtDescripcion=Entry(ven,font=("calibri",13,),width=9)
txtDescripcion.place(x=130,y=310)

txtCodProd1=Entry(ven,font=("calibri",13,),width=8)
txtCodProd1.place(x=40,y=350)

txtDescripcion1=Entry(ven,font=("caliri",13,),width=9)
txtDescripcion1.place(x=130,y=350)

txtCodProd2=Entry(ven,font=("calibri",13,),width=8)
txtCodProd2.place(x=40,y=390)

txtDescripcion2=Entry(ven,font=("calibri",13,),width=9)
txtDescripcion2.place(x=130,y=390)

txtUnidad=Entry(ven,font=("calibri",13,),width=8)
txtUnidad.place(x=230,y=310)

txtUnidad1=Entry(ven,font=("calibri",13,),width=8)
txtUnidad1.place(x=230,y=350)

txtUnidad2=Entry(ven,font=("calibri",13,),width=8)
txtUnidad2.place(x=230,y=390)


txtCantidad=Entry(ven,font=("calibri",13,),width=8)
txtCantidad.place(x=320,y=310)


txtCantidad1=Entry(ven,font=("calibri",13,),width=8)
txtCantidad1.place(x=320,y=350)

txtCantidad2=Entry(ven,font=("calibri",13,),width=8)
txtCantidad2.place(x=320,y=390)

txtPrecio=Entry(ven,font=("calibri",13,),width=8)
txtPrecio.place(x=405,y=310)

txtPrecio1=Entry(ven,font=("calibri",13,),width=8)
txtPrecio1.place(x=405,y=350)

txtPrecio2=Entry(ven,font=("calibri",13,),width=8)
txtPrecio2.place(x=405,y=390)

txtSubtotal=Entry(ven,font=("calibri",13,),width=8)
txtSubtotal.place(x=490,y=310)

txtSubtotal1=Entry(ven,font=("calibri",13,),width=8)
txtSubtotal1.place(x=490,y=350)

txtSubtotal2=Entry(ven,font=("calibri",13,),width=8,)
txtSubtotal2.place(x=490,y=390)

txtTotal=Entry(ven,font=("calibri",13,),width=8)
txtTotal.place(x=510,y=440)

#botones

btnProductos=Button(ven, text="Ver inf. productos", font=("calibri",12),command=verProd)
btnProductos.place(x=70,y=440)
btnProductos.config(bg="light gray")

btnMostrar=Button(ven, text="Mostrar cliente",font=("calibri",12),command=mostrar)
btnMostrar.place(x=140,y=225)
btnMostrar.config(bg="light gray")

btnAgregar=Button(ven, text="Agregar cliente",font=("calibri",12),command=agregar)
btnAgregar.place(x=350,y=225)
btnAgregar.config(bg="light gray")

btnLimpiar=Button(ven, text="Limpiar casillas",font=("calibri",12),command=Limpiar)
btnLimpiar.place(x=230,y=440)
btnLimpiar.config(bg="light gray")

btnCalcular=Button(ven, text="Calcular",font=("calibri",12),command=calcular)
btnCalcular.place(x=380,y=440)
btnCalcular.config(bg="light gray")

lista=[(txtCodProd, txtDescripcion, txtUnidad, txtPrecio),
       (txtCodProd1, txtDescripcion1, txtUnidad1, txtPrecio1),
       (txtCodProd2, txtDescripcion2, txtUnidad2, txtPrecio2)]


ven.mainloop()
