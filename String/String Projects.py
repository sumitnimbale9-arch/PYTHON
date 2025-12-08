# PROJECT 1: TEXT CASE CONVERTER
# def text_case_converter():
#     print("====TEXT ACSE CONVERTER====")
#     text = input("ENTER YOUR TEXT: ")

#     print("""
# choose an option:
# 1.CONVERT TO UPPERCASE
# 2.CONVERT TO LOWERCASE
# 3.CONVERT TO TITLE CASE
# 4.TOGGLE CASE
# """)
    
#     choice = input("ENTER YOUR CJOICE (1-4):")

#     if choice == "1":
#         print("\nUPPERCASE:" , text.upper())

#     elif choice == "2":
#         print("\nLOWERCASE:" , text.lower())

#     elif choice == "3":
#         print("\nTITLE CASE:" , text.title())

#     elif choice == "4":
#         print("\nTOGGLE CASE:" , text.swapcase())

#     else:
#         print("\n Invalid CHOICE! TRY AGAIN.")

# text_case_converter()



#PROJECT 2: STRING CASE CONVERTER
# text = input("ENTER SENTENCE:")
# print("\nUPPERCASE: " , text.upper())
# print("LOWERCASE: " , text.lower())
# print("TITLE CASE:" , text.title())
# print("CAPITALIZE:" , text.capitalize())
# print("SWAPCASE:" , text.swapcase())



#PROJECT 3:- WORD & CHARACTER COUNT

# text = input("ENTER YOUR TEXT")

# vowels = "aeiouAEIOU"
# vowel_count = 0
# consonant_count = 0
# digit_count = 0
# space_count = 0
# special_count = 0

# for char in text :
#     if char in vowels:
#         vowel_count += 1
#     elif char.isalpha():
#         consonant_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     elif char.isspace:
#         space_count += 1
#     else:
#         special_count += 1

# print("\n----TEXT ANALYSIS REPORT----")
# print("Total Characters:" , len(text))
# print("Chatacters (No Spaces):" , len(text.replace(" ","")))
# print("Total Words:" , len(text.split()))
# print("Vowels:" , vowel_count)
# print("Consonants:" , consonant_count)
# print("Digits:" , digit_count)
# print("Spaces:" , space_count)
# print("Special Characters:" , special_count)

# 4.PALINDROME CHECKER

# text = input("Enter text:")

# cleaned = ""
# for char in text:
#     if char.isalnum():
#         cleaned +=char.lower()

# if cleaned == cleaned[::-1]:
#     print("IT IS a palindrome")
# else:
#     print("It is NOT a palindrome")


# 5.ANAGRAM CHECKER(INTERMEDIATE)

str1 = input("ENTER FIRST STRING:")
str2 = input("ENTER SECOND STRING:")

def clean_string(s):