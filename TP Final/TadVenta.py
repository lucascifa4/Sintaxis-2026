def crearVenta():
    Ven=[0,"","","","",0.0,"",""]
    return Ven

def cargarVenta(Ven,cod,nom,act,op,pago,imp,fec,hora):
    Ven[0]=cod
    Ven[1]=nom
    Ven[2]=act
    Ven[3]=op
    Ven[4]=pago
    Ven[5]=imp
    Ven[6]=fec
    Ven[7]=hora

def VerCod(Ven):
    return Ven[0]

def VerNom(Ven):
    return Ven[1]

def VerAct(Ven):
    return Ven[2]

def VerOp(Ven):
    return Ven[3]

def VerPago(Ven):
    return Ven[4]

def VerImp(Ven):
    return Ven[5]

def VerFec(Ven):
    return Ven[6]

def VerHora(Ven):
    return Ven[7]

def ModCod(Ven,cod):
    Ven[0]=cod

def ModNom(Ven,nom):
    Ven[1]=nom

def ModAct(Ven,act):
    Ven[2]=act

def ModOp(Ven,op):
    Ven[3]=op

def ModPago(Ven,pago):
    Ven[4]=pago

def ModImp(Ven,imp):
    Ven[5]=imp

def ModFec(Ven,fec):
    Ven[6]=fec

def ModHora(Ven,hora):
    Ven[7]=hora

def asignarVen(v1,v2):
    v2[0] = v1[0]
    v2[1] = v1[1]
    v2[2] = v1[2]
    v2[3] = v1[3]
    v2[4] = v1[4]
    v2[5] = v1[5]
    v2[6] = v1[6]
    v2[7] = v1[7]









