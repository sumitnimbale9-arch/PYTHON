# # Assignment operatprs are used to assign values to variables.
# # (=) ----> ASSIGNMENT OPERATOR
# # (+=)----> ADDITION ASSIGNMENT
# (-=)----> SUBTRACTION ASSIGNMENT
# (*=)----> MULTIPLICATION ASSIGNMENT

# x = 10
# x += 5
# print(x)

# -----------PROJECT----------
# print("WELCOME TO THE SHOPPING CART !")

# total = 0 #total cart value
# discount = 0 #discount amount

# #Taking input for 3 items
# for i in range(1,6):
#     price = float(input(f"Enter price of item {i}:"))
#     qty = int(input(f"Enter quantity of items{i}:"))

#     item_total = price*qty
#     total += item_total 

#     print(f"Item {i} total: ₹{item_total}\n")

# # -------- GST Calculation --------
# GST_RATE = 0.18   # 18% GST

# gst_amount = total * GST_RATE
# grand_total = total + gst_amount


# #Apply discount based on conditions
# if total >= 2000:
#     discount = total * 0.20
# elif total >= 1000:
#     discount = total * 0.10
# else:
#     discount = 0

# final_amount = total; - discount

# print("------ BILL SUMMARY -----")
# print("CART TOTAL       :", total)
# print("DISCOUNT APPLIED       :", discount)
# print("FINAL PAYABLE       :", final_amount)

# WITH GST CODE
# print("Welcome to the Shopping Cart!")

# total = 0

# # Take 3 items (you can change this number)
# for i in range(1, 4):
#     price = float(input(f"Enter price of item {i}: "))
#     qty = int(input(f"Enter quantity of item {i}: "))

#     item_total = price * qty
#     total += item_total   # Add to cart using +=

#     print(f"Item {i} total: ₹{item_total}\n")

# # -------- GST Calculation --------
# GST_RATE = 0.18   # 18% GST

# gst_amount = total * GST_RATE
# grand_total = total + gst_amount

# # -------- Discount Conditions (Optional) --------
# if total >= 2000:
#     discount = total * 0.20      # 20% off
# elif total >= 1000:
#     discount = total * 0.10      # 10% off
# else:
#     discount = 0

# grand_total_after_discount = grand_total - discount

# # -------- Final Bill --------
# print("------ BILL SUMMARY ------")
# print("Cart Total (before GST):", total)
# print("GST (18%):              ", gst_amount)
# print("Total + GST:            ", grand_total)
# print("Discount Applied:       ", discount)
# print("----------------------------")
# print("Final Payable Amount:    ", grand_total_after_discount)


# WITH COUPON CODE
print("Welcome to the Shopping Cart!")

total = 0

# Taking input for 3 items
for i in range(1, 4):
    price = float(input(f"Enter price of item {i}: "))
    qty = int(input(f"Enter quantity of item {i}: "))

    item_total = price * qty
    total += item_total    # using +=

    print(f"Item {i} total: ₹{item_total}\n")

print("Cart Total (before coupon): ₹", total)

# ----- Coupon System -----
print("\nAvailable Coupons:")
print("SAVE10  → 10% off")
print("SAVE20  → 20% off (min purchase ₹2000)")
print("SUPER50 → Flat ₹50 off")
print("No coupon? Press Enter")

coupon = input("\nEnter coupon code: ").upper()

discount = 0

# ----- Coupon Conditions -----
if coupon == "SAVE10":
    discount = total * 0.10

elif coupon == "SAVE20":
    if total >= 2000:
        discount = total * 0.20
    else:
        print("SAVE20 requires minimum ₹2000 purchase. Coupon not applied.")

elif coupon == "SUPER50":
    discount = 50

elif coupon == "":
    print("No coupon applied.")

else:
    print("Invalid coupon code.")

final_amount = total - discount

# ----- Final Bill -----
print("\n------ BILL SUMMARY ------")
print("Cart Total:", total)
print("Discount :", discount)
print("Final Payable Amount:", final_amount)
