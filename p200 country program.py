india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

print("press1 for one city")
print("press2 for two city")
op = int(input("enter opt==>"))
if op == 1:

    city = (input("enter your city=>"))

    if city in india:
        print(city, "your city belongs to india")
    elif city in pakistan:
        print(city, "your city belongs to pakistan")
    elif city in bangladesh:
        print(city, "your city belongs to bangladesh")
    else:
        print("none of above")

elif op == 2:

    city1 = (input("enter your city1=>"))
    city2 = (input("enter your city2=>"))

    if city1 in india and city2 in india:
        print("they both are in same country")
    elif city1 in pakistan and city2 in pakistan:
        print("they both are in same country")
    elif city1 in bangladesh and city2 in bangladesh:
        print("they both are in same country")
    else:
        print("2.They don't belong to same country")