print("Bienvenido/a a este programa")

comprobar = True 

while comprobar == True: 

    num = int(input("Ingrese un numero entero positivo: "))

    if num > 0:
        resultado = 0 

        for i in range(1, num + 1): 
            resultado +=  (1/i)
        
        print("El resultado de esta serie es de: ", resultado)

    else: 
        print("El numero ingresado es incorrecto, porfavor intente de nuevo")
   
print("El programa ha finalizado")