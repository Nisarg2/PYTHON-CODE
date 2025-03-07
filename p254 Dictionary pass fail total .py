students={12:"ram",25:"jayul",35:"rahul",41:"ami",55:"riya",45:"hiral",33:"karan"}
c=0
d=0
for k,v in students.items():
    if k>35:
        print(k,"\t\t",v,"\t\t pass")
        c=c+1
    else:
        print(k,"\t\t",v,"\t\t fail")
        d=d+1
print("count of pass students=>",c)
print("count of fail student=>",d)
