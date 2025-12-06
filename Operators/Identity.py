# USED TO COMPARE THE MEMORYLOCATION OF TWO OBJECTS
# is - true for same location memory
# is not - 

# a = [1,2,3]
# b = a
# c = [1,2,3]

# print(a is b)
# print(a is c)

# vegetables = ['karela' , 'Aloo' , 'Tamatar']
# print('Bhindi' in vegetables)
# print('Aloo' in vegetables)

# item = input("Enter item: ")

# if item == "Banana":
#     print("Adding Banana to cart...")


# ---------------------------------------------------------
# LEVEL 2 PROJECT — SMART VEGETABLE INVENTORY SYSTEM
# Concepts: is, is not, in, not in, memory comparison
# ---------------------------------------------------------

# Main inventory list (original)
# main_inventory = ["Potato" , "Tomato" , "Onion" , "Carrot" , "Cabbage"]

# # Duplicate references (same memory)
# ref_inventory_A = main_inventory
# ref_inventory_B = main_inventory

# # Copy list (different memory)
# new_stock_list = ["Potato" , "Tomato" , "Onion" , "Carrot" , "Cabbage"]

# # ---------------- MEMORY IDENTITY CHECK -------------------

# print("MEMORY CHECK\n")

# print("A and B are in same memory?" , ref_inventory_A is ref_inventory_B)
# print("A and new_stock are in same memory?" , ref_inventory_A is new_stock_list)
# print("A and new_stock are in different memory?" , ref_inventory_A is not new_stock_list)

# print("\n----------------------------------------------------------------------")

# # ------------------- INVENTORY CHECK -----------------------
# user_item = input("Enter vegetable to check Availability: ")

# if user_item in main_inventory:
#     print(f"Yes, {user_item} is AVAILABLE.")
# else:
#     print(f"NO, {user_item} is NOT-AVAILABLE.")

# # ------------------- STALE / FRESH CHECK -------------------
# stale_items = ("Tomato" , "Cabbage")

# if user_item in stale_items:
#     print("WARNING : THE VEGETABLE IS STALE TODAY!!")
# else:
#     print("THE VEGETABLE IS FRESH")
 
# # ------------------- STOCK MISMANAGEMENT WARNING -------------------\
# if new_stock_list is main_inventory:
#     print("\n ERROR: STOCK LIST IS USING SAME MEMORY AS MAIN INVENTORY!")
# else:
#     print("\n SAFE: STOCK LIST IS A SEPERATE COPY.")



# ---------------------------------------------------------
# SMART VEGETABLE INVENTORY SYSTEM (UPGRADED VERSION)
# Features:
# ✔ Case-insensitive matching
# ✔ Partial search: "tom" → Tomato
# ✔ Synonyms: "aloo" → Potato
# ✔ Suggestions when spelling is wrong
# ---------------------------------------------------------
main_inventory = ["Potato" , "Tomato" , "Onion" , "Carrot" , "Cabbage"]

# Synonyms dictionary (normalized)
synonyms = {
    "aloo" :"Potato",
    "kanda" : "Onion",
    "gobhi" : "Cabbage",
}
# Normalize a word safely
def norm(word):
    return word.casefold().strip()




# ---------- 1) BUILD LOOKUP TABLE ----------

lookup = {}

# Add main inventory items
for item in main_inventory:
    lookup[norm(item)] = item

for key, value in synonyms.items():
    lookup[norm(key)] = value

    

    
# ---------- 2) USER INPUT ----------

user_raw = input("Enter vegetable name: ")
user_key = norm(user_raw)




# ---------- 3) DIRECT MATCH OR SYNONYM MATCH ----------
if user_key in lookup:
    print(f"AVAILABLE: {lookup[user_key]}")




else:
    # ---------- 4) PARTIAL MATCH SUGGESTIONS ----------
    partials = []
    for key, original in lookup.item():
         if key.startswith(user_key):
             partials.append(original)

    if partials:
        print("? DID YOU MEAN:")
        for item in set(partials):
             print("  ->" , item)
    else:
        print(f"x '{user_raw}' not found in inventory.")




        # ---------- 5) NEAREST SPELLING SUGGESTION ----------
        close_matches = []
        for key, original in lookup.items():
            if user_key[0] in key:
                close_matches.appemd(original)

        if close_matches:
            print("\nClosest matches I found:")
            for item in set(close_matches):
                print("  ->" , item)

        
                