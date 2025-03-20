marks={"ram": 33,"rahul": 15,"devesh": 30,"jayul": 34,"jiya": 16,"sadhana": 11,"meena": 19,"karan": 20}
c=0
d=0
for k,v in marks.items():
    if v >15:
         print(k,"\t\t",v,"\t\t pass")
         c=c+1
    else:
        print(k,"\t\t",v,"\t\t fail")
        d=d+1
print("count of pass students=>",c)
print("count of fail student=>",d)

