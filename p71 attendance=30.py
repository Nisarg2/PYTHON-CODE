lec=int(input("enter a lec"))
att=int(input("enter a att"))

attendance_percentage = (att / (lec)) * 100
if attendance_percentage >= 75 and attendance_percentage <100:
    print("The student is allowed to sit in the exam.")
elif attendance_percentage >100:
    print("error")
else:
    print("The student is not allowed to sit in the exam.")

