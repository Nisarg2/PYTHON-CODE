n = int(input("Enter a limit => "))
t = 0
c = 0
i = 1
while i <= n:
    if i % 2 == 0:
        print("even num =", i)
    else:
        print("odd num =", i)
    t = t + i
    c = c + 1
    i = i + 1

