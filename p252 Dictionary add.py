students={1:"ram",2:"jayul",3:"rahul",4:"anjali",5:"riya",12:"hiral",33:"karan"}
print(students)

students[3]="hiral"
print(students)

students.setdefault(101,"sita")
print(students)

students.setdefault(102,"")
students[102]="ravan"

print(students)