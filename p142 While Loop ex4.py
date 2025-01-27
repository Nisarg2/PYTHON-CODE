n = int(input("Enter a limit => "))
total = 0
i = n
while i > 0:
    print(i, end="X")
    total += i
    i -= 1
print("\ntotal sum", total)
