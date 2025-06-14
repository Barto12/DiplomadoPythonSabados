def promedio (a,b,c):
    return (a+b+c)/3

print("Promedio:", promedio(8,7,9))


#Verificar si un numero es multiplo de otro

def es_multiplo (x,y):
    return x % y == 0
print(es_multiplo(10,2)) #True
print(es_multiplo(10,3)) #Falso
