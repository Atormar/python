temp= int(input("¿cual es su temperatura?:"))
if temp<0:
    print("hielo")
else:
    if temp<50:
        print("liquido")
    else:
        print("gaseoso")