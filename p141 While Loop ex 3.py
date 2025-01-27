num = 1
result = ""
n=int(input("enter a number"))
while num <= n:
    result += str(num)
    if num < n:
        result += "X"
    num += 1
print(result)
