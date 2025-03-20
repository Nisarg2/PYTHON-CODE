country={"china":143,"india":136,"usa":32,"uk":21}

print("press 1 for print country in  population")
print("press 2 for add country in population")
print("press 3 for remove in population ")
print("press 4 for query in population ")
op=int(input("enter a number"))

if op==1:
    print(country)

elif op==2:
    new_data = input("enter your data=>")
    key = int(input("enter key =>"))
    if new_data in country:
        print("its already exist")

    else:
        country[key] = new_data
        print(country)

elif op==3:
    remove_country = (input("enter country who to remove=>"))
    if remove_country in country:
        country.pop(remove_country)
        print(country)
    else:
        print("that country doesn't exist")

elif op==4:
    query_country = (input("enter query country=>"))

    for k, v in country.items():
        if query_country == k:
            print(k, "\t \t", v)
    else:
         print("that country doesn't exist")
