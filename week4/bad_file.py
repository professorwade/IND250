def funct4(x,y):
    print(x/y)

def funct3(x,y):
    if y == 0:
        raise ZeroDivisionError("I don't like zero!")
    funct4(x,y)

def funct2(x,y):
    funct3(x,y)

def funct1():
     while True:
        try:
            x = int(input("Enter an integer: "))
            y = int(input("Enter an integer: "))
            funct2(x,y)
            # what if code is here and an exception throws above here?
        except Exception as e:
            print(e)
            break
        else:
            print("whew, no error!")
        finally:
            print("I print with or without exception!")
funct1()