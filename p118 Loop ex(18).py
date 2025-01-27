for km in range(1, 6):
    answer = input(" Are you tired? (yes/no): ")
    if answer == "yes":
        print("You didn't finish the race.")
        break
    elif answer == "no":
        pass
    else:
        print("'yes' or 'no'.")
        pass
else:
    print("Congratulations You finished the 5 km race!")
