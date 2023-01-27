NumEle:int 

while True:
    try:
        NumEle= int(input("Elija un numero positivo y sin decimal"))
        break


    except ValueError:
        print("solo queremos numeros")

if NumEle < 1:
    print("Error no queremos numeros negativos") 

factorial=1 
if NumEle !=0:
    for i in range(1,NumEle+1):
        factorial=factorial*i
    print("Su factorial es:",factorial)    