import random
employe = {}
print("press 1 for all")
print("press 2 for specific salary")
print("press 3 for print the high salary")
no = int(input("enter the limits=>"))

if no == 1:
    n = int(input("Enter limit =>"))

    for i in range(1, n + 1):
        eno = i
        esalary = random.randint(10000, 50000)
        employe[eno] = esalary

    print("Eno\t\tEsalary")
    for k, v in employe.items():
        print(k, "\t\t", v)

elif no == 2:
    no = int(input("enter the num==>"))
    for i in range(1,no+1):
        eno = i
        esalary = random.randint(10000, 50000)
        employe[eno] = esalary

    for k, v in employe.items():
        if k == no:
            print(k, "\t\t", v)

elif no == 3:
    no = int(input("enter the num==>"))
    for i in range(1, no + 1):
        eno = i
        esalary = random.randint(10000, 50000)
        employe[eno] = esalary

    for k, v in employe.items():
        if v > 15000:
            print(k, "\t\t", v, "high salary")