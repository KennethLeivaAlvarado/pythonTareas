#Factoriales de los numeros ingresados 


#primero alguna manera recibir el input necesario
NumEle:int 

while True:
    try:
        NumEle= int(input("Elija un numero positivo y sin decimal"))
        break


    except ValueError:
        print("solo queremos numeros")

#confirmar que el numero es mayor a 0
if NumEle < 1:
    print("Error no queremos numeros negativos")  

#hacer que el programa sea capas de sacar el factorial del numeo dado o input
factorial=1 
if NumEle !=0:
    for i in range(1,NumEle+1):
        factorial=factorial*i
    print("Su factorial es:",factorial)

    



