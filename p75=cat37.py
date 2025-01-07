cat=int(input("enter a cat"))
if cat <18.5:
    print("bmi is undeweight")
elif cat<18.5 and cat<24.9:
    print("bmi is normal")
elif cat<25 and cat<29.9:
    print("bmi is overweight")
elif cat >30:
    print("bmi is obese")
else:
    print("error")