def add():
    print("1.ADDITION NUMBER")
    no1 = int(input("enter no1=>"))
    no2 = int(input("enter no2=>"))
    add = no1 + no2
    print("Add=", add)  # resusablity

def max2():
    print("2.MAX2 NUMBER")
    no1 = int(input("enter no1=>"))
    no2 = int(input("enter no2=>"))
    if no1 > no2:
        print("no1 is reater")
    else:
        print("no2 is greater")

def table():
    print("3.TABLE")
    n = int(input("enter a limit=>"))
    for i in range(1, 11):
        print(n, "X", i, "=", n * i)

def oddeven():
    print("4.ODD-EVEN NUMBER")
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print(" is Even".format(num))
    else:
        print(" is Odd".format(num))

def postneg():
    print("5.POSTIVE-NEGATIVE NUMBER")
    num=int(input("enter a number"))
    if num>0:
        print("posative")
    else:
        print("negative")

def areaoftriangle():
    print("6.AREA OF TRIANGLE ")
    b=int(input("enter a height"))
    h=int(input("enter a weight"))
    print("area of triangle=",0.5* h * b)

def areaofcircle():
    print("7.AREA OF CIRCLE ")
    radius=0
    radius=int(input("enter a radius"))
    print("area of circle=", 3.14 * radius * radius)

def max3():
    print("8.MAX3 NUMBER")
    num1 = int(input("enter num1=>"))
    num2 = int(input("enter num 2=>"))
    num3 = int(input("enter num3=>"))
    if num1 > num2 and num1 > num3:
        print("num1 is grater than num3 and num2")
    elif num2 > num3 and num2 > num1:
        print("num2 is grater than num1 and num3")
    elif num3 > num2 and num3 > num1:
        print("num3 is grater than num2 and num1")
    else:
        print("all are equal")

def cube():
    print("9.CUBE NUMBER")
    no=int(input("enter a number"))
    print("cube=",no*no*no)

def simpleint():
    print("10.SIMPLEINT NUMBER")
    p = int(input("Enter principle value =>"))
    r = float(input("Enter rate =>"))
    t = int(input("Enter time =>"))
    print("intrest of 2 year=", p * r * t / 100)

def factorial():
    print("11.FACTORIAL NUMBER")
    n = int(input("enter a limit=>"))
    for i in range(n,0,-1):
        print(i*i,end="-")

add()
max2()
table()
oddeven()
postneg()
areaoftriangle()
areaofcircle()
max3()
cube()
simpleint()
factorial()
