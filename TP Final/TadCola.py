def crearCola():
    cola=[]
    return []

def esVaciaCola(cola):
    return len(cola) == 0

def encolar(cola, Ven):
    cola.append(Ven)

def desencolar(cola):
    Ven = cola[0]
    del cola[0]
    return Ven

def tamanioCola(cola):
    return len(cola)