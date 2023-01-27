while True:
    try:
        NumElec=int(input("Elija un numero"))
        break
    
    except ValueError:
        print("Solo queremos numeros")
        continue

if NumElec<1:
    print("No queremos numeros negativos")
    
else:
    concatenado=""
    for i in range(1,NumElec+1):
        concatenado=''.join([concatenado, str(i)])
        print(concatenado)