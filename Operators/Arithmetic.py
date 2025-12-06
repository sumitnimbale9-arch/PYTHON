# x = 10
# y = 20

# print(x+y) #addition
# print(x-y)  #subtraction
# print(x*y)  #multiplication
# print(x/y)  #division
# print(x//y) #floor division
# print(x%y)  #modulus- remainder
# print(x**y) #power calculation


print("-------ATM CASH SIMULATOR-------")

balance = float(input("ENTER YOUR STARTING BALANCE:"))

pin = int(input("SET A 4-DIGIT ATM PIN:"))
encrypted_pin = pin ** 3
print ("Your Encrypted PIN Stored as:" , encrypted_pin)

deposit = (float(input("ENTER DEPOSIT AMOUNT :")))
Balance = balance + deposit

withdraw = (float(input("AMOUNT TO BE WITHDRAWED:")))

if withdraw <= balance:
    balance = balance - withdraw
    print("/nCash Withdrawal Successful!!")

    # Step 5: Breakdown into notes using arithmetic operators
    print("\n--- NOTE BREAKDOWN ---")
     
    amt = withdraw

    n2000 = amt // 2000
    amt = amt%2000

    n500 = amt // 500
    amt = amt%500

    n200 = amt//200
    amt = amt%200

    n100 = amt//100
    amt = amt%100

 
    print("2000 x", int(n2000))
    print("500  x", int(n500))
    print("200  x", int(n200))
    print("100  x", int(n100))
else:
    print("INSUFFICIENT BALANCE!!")

# Step 6: Show final balance
print("\nRemaining Balance:", balance)
