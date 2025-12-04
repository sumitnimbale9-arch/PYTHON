##✅ LEVEL 1 — Basic Break Project
#  for num in range(1, 10, 1):
#     if num == 5:
#         break

#     print(num)

# ✅ LEVEL 2 — Break in User Input

# while True:
#     word = input("Enter a word: ")

#     if word.lower().casefold().strip() == "quit":
#         print("Loop Ended.")
#         break
    
#     print("Processing...")


# -----------------------------
# ✅ LEVEL 3 — Break With Searching
# -----------------------------

# fruits = ["apple" , "mango" , "banana" , "orange"]

# for index in range(len(fruits)):
#     if fruits[index] == "mango":
#         print(f"Found at index {index}")
#         break


# -----------------------------
# ✅ LEVEL 4 — Break + Flags
# -----------------------------

# transactions = [5000, 12000, 35000, 800000, 150000, 7000]

# fraud_detected = False
# fraud_amount = None

# for amount in transactions:
#     if amount > 1000000:
#         fraud_detected = True
#         fraud_amount = amount
#         break

# if fraud_detected:
#     print(f"FRAUD DETECTED AT TRANSACTION AMOUNT:  ₹{fraud_amount}")
# else:
#     print("ALL TRANSACTIONS SAFE.")



# PROJECT 1:PASSWORD VALIDATOR
# Real-world use:Input validation in ML Pipelines

# print("=" * 60)
# print("PROJECT 1 : PASSWORD VALIDATOR")
# print("=" * 60)

# def password_validator():
#     max_attempts = 3
#     attempt = 0

#     while attempt < max_attempts:
#         password = input("ENTER PASSWORD: ")

#         # Conditions
#         has_upper = any(c.isupper() for c in password)
#         has_lower = any(c.islower() for c in password)
#         has_digit = any(c.isdigit() for c in password)
#         has_special = any(c in "!@#$%^&*" for c in password)
#         is_long = len(password) >= 8

#         # If all conditions satisfied
#         if all([has_upper, has_lower, has_special, has_digit, is_long]):
#             print("PASSWORD ACCEPTED!")
#             break

#         # Else show errors
#         else:
#             attempt += 1
#             print(f"Invalid Password. Attempt {attempt}/{max_attempts}")
            
#             if not is_long: print(" - Need at least 8 characters")
#             if not has_upper: print(" - Need Uppercase Letter")
#             if not has_lower: print(" - Need Lowercase Letter")
#             if not has_digit: print(" - Need Digit")
#             if not has_special: print(" - Need Special Character (!@#$%^&*)")

#     # If loop finishes without break
#     if attempt == max_attempts:
#         print("TOO MANY FAILED ATTEMPTS!")

# # 🚀 Run the program
# password_validator()

# 
# PROJECT 2: ATM WITHDRAWAL SIMULATOR
# Real-world use: State management in ML training loops

# print("\n" + "="*60)
# print("PROJECT 2: ATM WITHDRAWAL SIMULATOR")
# print("="*60)

# def atm_simulator():
#     balance = 1000

#     while True:
#         print(f"\n CURRENT BALANCE: ${balance}")
#         print("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit")
         
#         choice = input("Choose option: ")

#         if choice == "1":
#             amount = float(input("ENTER WITHDRAWAL AMOUNT: $"))
#             if amount > balance:
#                 print("INSUFFICIENT FUNDS!")
#             else:
#                 balance -= amount
#                 print(f"Withdraw ${amount}. New balance${balance}")
#         elif choice == "2":
#             amount = float(input("ENTER DEPOSIT AMOUNT: $"))
#             balance += amount
#             print(f"Deposited ${amount}. New balce: {balance}")

#         elif choice == "3":
#             print(f"Your Balance is: ${balance}")

#         elif choice == "4":
#             print("Thank you for using ATM!")
#             break

#         else:
#             print("INVALID OPTION!")
# atm_simulator()




