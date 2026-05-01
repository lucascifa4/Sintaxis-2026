def crearAgencia():
    Agencia=[]
    return Agencia

def agregarVenta(Agencia, Ven):
    Agencia.append(Ven)

def eliminarVenta(Agencia, Ven):
    Agencia.remove(Ven)

def recuperarVenta(Agencia, i):
    return Agencia[i]

def tamanio(Agencia):
    return len(Agencia)