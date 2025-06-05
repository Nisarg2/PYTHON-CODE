try:
    no1=int(input("enter a number 1=>"))
    no2=int(input("enter a number 2=>"))
    print("sum = ",no1/no2)
except ValueError:
    print("Why u enter string")
except ZeroDivisionError:
    print("Why u enter 0")
except:
    print("Error")