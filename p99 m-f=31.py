age=(int(input("enter the age ==>")))
gender=input("enter the gender==>")

if gender=="female":
    print("she will work only in urban areas.")

elif gender=="male":
    if age >=20 and age<=40:
        print("he may work anywhere.")
    elif age>40 and age <60:
        print("he will work in urban areas only.")
else:
    print("ERROR")