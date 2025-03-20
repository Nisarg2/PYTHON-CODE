my_expennse={"clothes":1100,"shoes":1000,"watch":900,"recharge":699,"petrol":1980}

wife_expense={"recharge":799,"dth recharge":999,"clothes":2310,"makeup":3670,"shoes":999}

my_total_expense=sum(my_expennse.values())
wife_total_expense=sum(wife_expense.values())

print("my total expense==>",my_total_expense)
print("wife total expense==>",wife_total_expense)


if my_total_expense>wife_total_expense:
    print("i'm spending more.")

elif wife_total_expense>my_total_expense:
    print("\n\t wife spendinng more.")

else:
    print("\n\t we are spending same amount.")

list1 = []

for k, v in my_expennse.items():
    list1.append(v)

maxvalue = max(list1)

for k, v in my_expennse.items():

    if maxvalue == v:
        print("my expennse=>",k, v)

list1 = []

for k, v in wife_expense.items():
    list1.append(v)

maxvalue = max(list1)

for k, v in wife_expense.items():

    if maxvalue == v:
        print("wife expense=>",k, v)