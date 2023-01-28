#Triangulo de numeros

#primero una forma en la que el usuario elija un numero
while True:
    try:
        NumElec=int(input("Elija un numero"))
        break
    #validacion de solo numeros
    except ValueError:
        print("Solo queremos numeros")
        continue
#validacion de que el numero es mayor a 0
if NumElec<1:
    print("No queremos numeros negativos")
    #que los numeos aparescan segun el input en piramide 
else:
    concatenado=""
    for i in range(1,NumElec+1):
        concatenado=''.join([concatenado, str(i)])
        print(concatenado)