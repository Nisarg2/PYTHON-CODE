n = int(input("enter a limit"))
total = 0

for i in range(1, n + 1):
    if i % 7 == 0:
        print(i)
        total = total + i
print("total",total)
