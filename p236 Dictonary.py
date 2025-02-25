d1 = {11: "ram", 13: "mohan", 15: "rahul", 66: "dev",21: "sita", 25: "geeta", 30: "arjun", 45: "krishna", 50: "radha"}
d1[55] = "shyam"
d1[60] = "lakshman"

for k,v in d1.items():
    if len(v)<5:
        print(k,v)