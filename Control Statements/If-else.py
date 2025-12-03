# age =int(input("ENTER YOUR AGE = "))
# if age >= 18:
#     print("YOU  CAN VOTE")
# else:
#     print("YOU ARE <18")

# ---------------PROJECTS-------------------
# -----PROJECT-1-----
# temp = float(input("Enter Temperature in °C:"))

# if temp <= 0:
#     print("Freezing")
# elif temp <= 20:
#     print("Cold")
# elif temp <= 30:
#     print("Warm")
# else:
#     print("HOT")



# -----PROJECT-2-----
# marks = int(input("ENTER YOUR MARKS:"))

# if marks > 100 or marks < 0 :
#     print("INVALID MARKS")
# elif marks >= 90:
#     print("GRADE-A")

# if marks > 95:
#     print("DISTINCTION!!")
# elif marks >= 75:
#     print("GRADE-B")
# elif marks >= 60:
#     print("GRADE C")
# elif marks >=35:
#     print("GRADE-D")
# else:
#     print("FAIL")



# # ------------------------------
# -----!!PROJECT-3!!-----
# # ------------------------------

# correct_pin = 1234
# balance = 10000

# pin = int(input("ENTER PIN:"))

# if pin != correct_pin:
#     print("X INVALID PIN ENTERED. ACCESS DENIED")
# else:
#     amount = int(input("ENTER AMOUNT TO BE WITHDRAW:"))

#     if amount <= 0:
#         print("X INVALID AMOUNT")
#     elif amount > balance:
#         print("INSUFFICIENT BALANCE")
#     else:
#         balance -= amount
#         print(f"WITHDRAWAL SUCCESSFUL!! REMAINING BALANCE: {balance}")



# # ------------------------------
# -----!!PROJECT-4!!-----
# # ------------------------------

# print("=== LOAN ELIGIBILITY SYSTEM ===")

# age = int(input("ENTER YOUR AGE:"))
# income = int(input("ENTER INCOME:"))
# cibil = int(input("ENTER CIBIL SCORE:"))
# has_loan = input("Do you have any existing loan? (YES/NO): ").strip().casefold()

# # 1. HIGH RISK INSTANT REJECTION
# if age <= 18:
#     print("❌ LOAN REJECTED: AGE BELOW 18")
# elif income < 15000:
#     print("❌ LOAN REJECTED: INCOME BELOW 15000")
# elif cibil < 550:
#     print("❌ LOAN RAHJECTED: CIBIL BELOW 550")

# # 2. GENERAL ELIGIBILITY CHECK
# elif not (21 <= age <= 60):
#     print("❌ Loan Rejected: Age must be between 21 and 60")
# elif income < 25000:
#     print("❌ LOAN REJECTED: MINIMUM INCOME REQUIRED IS ₹25,000") 
# elif cibil < 700:
#     print("❌ LOAN REJECTED: CIBIL Score must be 700 or above")

# # 3.EXISTING LOAN CASE
# elif has_loan == "YES":
#     if income >= 40000:
#         print("⚠️ Loan Approved With Conditions (EXISTING LOAN DETECTED)")
#     else:
#         print("❌ Loan Rejected : Existing Loan and Low Income")

# # 4.FULL APPROVAL
# else:
#     print("LOAN APPROVED SUCCESSFULLY!!")



