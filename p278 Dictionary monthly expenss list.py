month={"jan":2200,"feb":2350,"march":2600,"april":2130,
       "may":2190,"june":1980,"july":2400,"aug":2250,
       "sept":2100,"oct":2400,"nov":2150,"dec":2500}

"1.	In February, how many dollars did you spend extra compared to January?"
v1=month["feb"]
v2=month["jan"]
d=v1-v2
print("Diffrence of NO.1 =>",d)


"2.	Calculate your total expenses for the first quarter (January to March) of the year."
v1=month["jan"]
v2=month["feb"]
v3=month["march"]
d=v1+v2+v3
print("addition of NO.2 =>",d)


"3.	Check if you spent exactly 2400 dollars in any month."
c=0
for k,v in month.items():
       if v==2400:
        print("ectly month of NO.3=>",k,v)


"4.Modify the expense for June (2080 dollars) to your monthly expenses."
month["june"]=2080
print("modfiy value for june NO.4=>",month["june"])


"5.You returned an item that you bought in April and received a refund of 200 dollars. "
v=month["april"]
v=month["april"]=v-200
print("returned dollars for april NO.5=>",month["april"])


"6.	Determine which month had the highest expense and print the month "
list1=[]

for k,v in month.items():
    list1.append(v)

maxvalue=max(list1)

for k,v in month.items():
    if maxvalue==v:
        print("highest expense of NO.6=>",k,v)


"7.	Calculate the average monthly expense for the first half of the year (January to June)."
Month = {"jan":2200,"feb":2350,"march":2600,"april":2130,"may":2190,"june":1980}
average = sum(Month.values()) / len(Month)

print("Average of 6 month NO.7=>:", average)


"8.	Find the month with the lowest expense and print the month and the amount."
list1=[]

for k,v in month.items():
    list1.append(v)

minvalue=min(list1)

for k,v in month.items():
    if minvalue==v:
        print("lowest expense of NO.8=>",k,v)