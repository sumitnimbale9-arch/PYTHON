# multiple conditions combined -Boolean True/False
 
# add - all conditions must be true > True\
# or - atleast one condition > True
# not - single operand, reversed

a = 10
b = 20

print(a>5 and b>10)
print(a<1 or b == 20)
print(not(a==10))


# PASSWORD PROJECT
# 1. INPUT password

# 2. CHECK character types:
#     - lowercase?
#     - uppercase?
#     - digit?
#     - special char?

# 3. CHECK length:
#     - < 8 → Weak
#     - >= 8 → continue checks

# 4. STRONG password check:
#     IF (length >= 8)
#        AND (has_lower AND has_upper)
#        AND (has_digit OR has_special)
#        → Strong

# 5. ELSE → Moderate

# 6. Print suggestions using `not` conditions

password = input("ENTER YOUR PASSWORD :")

# Conditions using: and, or, not, in, length
has_lower = False
has_upper = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()-_=+[]{};:,.<>?/"

#check each character 

for ch in password:
    if ch.islower():
        has_lower = True
    elif ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True

# Strength logic
if len(password) < 8:
    strength = "Weak"
elif len(password) >= 8 and (has_lower and has_upper) and (has_digit or has_special):
    strength = "strong"
else:
    strength = "Moderate"

# print result
print("\nPassword Strength:", strength)

# Detailed reasons
print("Details:")
if not has_lower:
    print("- Add lowercase letters")
if not has_upper:
    print("- Add uppercase letters")
if not has_digit:
    print("- Add digits (0-9)")
if not has_special:
    print("- Add special characters (!@#$ etc.)")
if len(password) < 12:
    print(" - Increase length to 12+ for best security")