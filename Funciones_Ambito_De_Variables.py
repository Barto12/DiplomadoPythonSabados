# ambito de variables  :declarar una variable global

x = 10 # global

def prueba():
    x = 5 # local
    print("Dentro:", x)

    prueba()
    print("Fuera:", x)
    