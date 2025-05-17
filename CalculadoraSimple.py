# Ejercicio Calculadora Simple

num1 = float(input("Ingresa el primer numero: "))

num2 = float(input("Ingresa el segundo numero: "))

operacion = (input("Elige la operacion (+,-, *, /: "))

if operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "-":
    print("Resultado:", num1 - num2)
elif operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "/":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("No se puede dividir entre cero.")
else:
  print("Operacion no valida")






