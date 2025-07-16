def interpreter():
    x,y,z=input("expression: ").split()
    x=int(x)
    z=int(z)
    if(y=="+"):
        result=float(x+z)
        print(f"{result:.1f}")
    elif(y=="-"):
        result=float(x-z)
        print(f"{result:.1f}")
    elif(y=="/"):
        if(z>0):
            result=float(x/z)
            print(f"{result:.1f}")
        else:
            print("z should be greater than zero")
    elif(y=="*"):
        result=float(x*z)
        print(f"{result:.1f}")
    else:
        print("enter the operators(+,-,/,*)")
interpreter()



