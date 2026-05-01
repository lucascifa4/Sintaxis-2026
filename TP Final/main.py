from TadAgencia import *
from TadAgencia import *
from TadVenta import *

#Creo agencia
ag = crearAgencia()
#Creo ventas
for i in range(2):
    print("creacion de venta ",i+1)
    v = crearVenta()
    cod=input("Ingrese el codigo de la excursion: ")
    nom=input("Ingrese el nombre del servicio: ")
    act=input("Ingrese la actividad: ")
    op=input("Ingrese el operador turistico: ")
    pago=input("Ingrese el metodo de pago: ")
    imp=float(input("Ingrese el importe: "))
    fec=input("Ingrese la fecha: ")
    hora=input("Ingrese la hora: ")
    cargarVenta(v,cod,nom,act,op,pago,imp,fec,hora)
    agregarVenta(ag,v)
    print("--------------------------------------------------")

#Muestro ventas
for i in range(tamanio(ag)):
    v = recuperarVenta(ag,i)
    print("numero de cliente ",i+1)
    print("Codigo: ",VerCod(v))
    print("Nombre: ",VerNom(v))
    print("Actividad: ",VerAct(v))
    print("Operador turistico: ",VerOp(v))
    print("Metodo de pago: ",VerPago(v))
    print("Importe: ",VerImp(v))
    print("Fecha: ",VerFec(v))
    print("Hora: ",VerHora(v))
    print("--------------------------------------------------")    

#Permitir la modificación de una venta existente, identificada por el Nombre del Servicio
nombre=input("Ingrese el nombre del servicio para modificar su venta: ")
for i in range(tamanio(ag)):
    v=recuperarVenta(ag,i)
    if VerNom(v)==nombre:
        #solo puedo modificar el metodo de pago y el importe por ahora
        pago= input("ingrese nuevo metedo de pago:")
        ModPago(v,pago)
        imp = float(input("ingrese nuevo importe:"))
        ModImp(v,imp)

for i in range(tamanio(ag)):
    v = recuperarVenta(ag,i)
    print("numero de cliente ",i+1)
    print("Codigo: ",VerCod(v))
    print("Nombre: ",VerNom(v))
    print("Actividad: ",VerAct(v))
    print("Operador turistico: ",VerOp(v))
    print("Metodo de pago: ",VerPago(v))
    print("Importe: ",VerImp(v))
    print("Fecha: ",VerFec(v))
    print("Hora: ",VerHora(v))
    print("--------------------------------------------------")    

#Permitir la eliminación de una venta a partir del Código de Excursión.
i = 0
while i < tamanio(ag):
    v=recuperarVenta(ag,i)
    print("venta recuperadada ",v)
    cod=input("Ingrese Código de Excursión para eliminar su venta: ")
    if VerCod(v)==cod:
        eliminarVenta(ag,v)
        print("Venta eliminada")
    i+=1


for i in range(tamanio(ag)):
    v = recuperarVenta(ag,i)
    print("numero de cliente ",i+1)
    print("Codigo: ",VerCod(v))
    print("Nombre: ",VerNom(v))
    print("Actividad: ",VerAct(v))
    print("Operador turistico: ",VerOp(v))
    print("Metodo de pago: ",VerPago(v))
    print("Importe: ",VerImp(v))
    print("Fecha: ",VerFec(v))
    print("Hora: ",VerHora(v))
    print("--------------------------------------------------")    


