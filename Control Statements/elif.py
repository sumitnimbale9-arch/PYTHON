age = int(input("ENTER YOUR AGE: "))
if (age >= 18 and age < 101):
    print("YPU CAN VOTE!")
elif age >= 101:
    print("GREATER THAN 101")
elif age <= 0:
    print("INVALID AGE")
else:
    print("ERROR OCCURED")