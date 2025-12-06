# print("-----ATM CARD SIMULATOR-----")

# balance = float(input("Enter Current balance:"))

# pin = int((input("SET A 4-DIGIT PIN:")))
# encrypted_pin = pin ** 4
# print("YOUR ENCRYPTED PIN IS :", encrypted_pin)

# deposit = float(input("ENTER AMOUNT TO BE DEPOSITED:"))
# Balance = balance + deposit
# print("AVAILABLE BALANCE IS :" , Balance)

# withdraw = (float(input("ENTER AMOUNT TO BE WITHDRAWED:")))

# if withdraw <= balance :
#     balance = balance - withdraw
#     print("/nCash Withdarwal successful:")

#     # REQUIRED NOTES.

#     amt = withdraw

#     n2000 = amt//2000
#     amt = amt%2000

#     n500 = amt//500
#     amt = amt%500

#     n100 = amt//100
#     amt = amt%100

#     n50 = amt//50
#     amt = amt%50

#     print("2000 x" ,int(n2000))
#     print("500 x" , int(n500))
#     print("100 x", int(n100))
#     print("50 x" , int(n50))

# else:
#     print("INSUFFICIENT BALANCE")






# #  PROJECT: “SCHOOL MARKSHEET & ANALYZER”

# print("-------STUDENT MARKSHEET-------")

# # INPUT MARKS
# m1 = int (input("Enter marks for subject 1: "))
# m2 = int (input("Enter marks for subject 2: "))
# m3 = int (input("Enter marks for subject 3: "))
# m4 = int (input("Enter marks for subject 4: "))
# m5 = int (input("Enter marks for subject 5: "))

# total = m1 + m2 + m3 + m4 + m5

# average = total / 5

# percentage = (total * 100) / 500

# max_score = 500
# marks_lost = max_score - total

# blocks_of_10 = total // 10
# remaining  = total % 10

# rank_score = total ** 2

# # Step 8: Display results
# print("\n----- RESULT -----")
# print("Total Marks:", total)
# print("Average Marks:", average)
# print("Percentage:", percentage)
# print("Marks Lost:", marks_lost)
# print("10-mark blocks:", blocks_of_10)
# print("Remaining Marks in the last incomplete block:", remaining)
# print("Rank Score (fun metric):", rank_score)







# print("----- STUDENT MARKSHEET (LEVEL 2) -----")

# #step 1 : INPUT MARKS FOR 5 SUBJECTS
# m1 = int(input("ENTER MARKS FOR SUBJECT 1:"))
# m2 = int(input("ENTER MARKS FOR SUBJECT 2:"))
# m3 = int(input("ENTER MARKS FOR SUBJECT 3:"))
# m4 = int(input("ENTER MARKS FOR SUBJECT 4:"))
# m5 = int(input("ENTER MARKS FOR SUBJECT 5:"))

# #STEP 2 : BASI CCALCULATIONS

# Total = m1 + m2 + m3 + m4 + m5

# Average = Total / 5

# percentage = (Total * 100) / 500

# marks_lost = 500 - Total

# # Step 3: Bonus Marks Logic

# if percentage >= 85:
#     bonus = 5
# else:
#     bonus = 0

# final_Total = Total + bonus
# final_percentage = (final_Total * 100) / 500

# # Step 4: Grade System

# if final_percentage >= 90:
#     grade = "A+"
# elif final_percentage >=80:
#     grade = "A"
# elif final_percentage >= 70:
#     grade = "B"
# elif final_percentage >= 60:
#     grade = "C"
# elif final_percentage >= 50:
#     grade = "D"
# else:
#     grade = "F"

# # Step 5: Pass/Fail Logic (fail if any subject < 33)

# if m1 < 33 or m2 < 33 or m3 < 33 or m4 < 33 or m5 < 33:
#     result = "FAIL"
# else:
#     result = "PASS"

# # Step 6: Distinction Check
# if final_Total >= 75 and result == "PASS":
#     distinction = "YES"
# else:
#     distinction = "NO"

# # Step 7: Display Output

# print("\n----- RESULT -----")
# print("Total Marks:", Total)
# print("Bonus Marks Applied:", bonus)
# print("Final Total:", final_Total)
# print("Final Percentage:", final_percentage)
# print("Grade:", grade)
# print("Pass/Fail:", result)
# print("Distinction:", distinction)
# print("Marks Lost:", marks_lost)





# LEVEL 3 PROJECT: “3-Student Performance Comparator + Ranking System”

# print("----- LEVEL 3: 3 STUDENT PERFORMANCE COMPARATOR -----")

# # ------------------------------
# # Step 1: Input marks for 3 students
# # ------------------------------

# print("/n-----Enter MARKS FOR STUDENT A-----")
# a1 = int(input("Subject 1: "))
# a2 = int(input("Subject 2: "))
# a3 = int(input("Subject 3: "))
# a4 = int(input("Subject 4: "))
# a5 = int(input("Subject 5: "))

# print("/n-----Enter MARKS FOR STUDENT B-----")
# b1 = int(input("Subject 1: "))
# b2 = int(input("Subject 2: "))
# b3 = int(input("Subject 3: "))
# b4 = int(input("Subject 4: "))
# b5 = int(input("Subject 5: "))

# print("/n-----Enter MARKS FOR STUDENT C-----")
# c1 = int(input("Subject 1: "))
# c2 = int(input("Subject 2: "))
# c3 = int(input("Subject 3: "))
# c4 = int(input("Subject 4: "))
# c5 = int(input("Subject 5: "))

# # ------------------------------
# # Step 2: Total / Percentage for each student
# # ------------------------------

# A_total = a1 + a2 + a3 + a4 + a5
# B_total = b1 + b2 + b3 + b4 + b5
# C_total = c1 + c2 + c3 + c4 + c5

# A_percentage = (A_total * 100) / 500
# B_percentage = (B_total * 100) / 500
# C_percentage = (C_total * 100) / 500


# # ------------------------------
# # Step 3: Pass/Fail (fail if any one subject < 33)
# # ------------------------------

# if a1 < 33 or a2 < 33 or a3 < 33 or a4 <33 or a5 <33:
#     A_result = "FAIL"
# else:
#     A_result = "PASS"

# if b1 < 33 or b2 < 33 or b3 < 33 or b4 <33 or b5 <33:
#     B_result = "FAIL"
# else:
#     B_result = "PASS"

# if c1 < 33 or c2 < 33 or c3 < 33 or c4 <33 or c5 <33:
#     C_result = "FAIL"
# else:
#     C_result = "PASS"

    
# # ------------------------------
# # Step 4: Distinction System
# # ------------------------------

# if A_total >= 74 and A_result == "PASS":
#     A_distinction = "YES"
# else:
#     A_distinction = "NO"

# if B_total >= 74 and B_result == "PASS":
#     B_distinction = "YES"
# else:
#     B_distinction = "NO"

# if C_total >= 74 and C_result == "PASS":
#     C_distinction = "YES"
# else:
#     C_distinction = "NO"

# # ------------------------------
# # Step 5: Ranking System (Rank 1, 2, 3)
# # ------------------------------

# # Find highest
# if A_percentage >= B_percentage and A_percentage >= C_percentage:
#     rank1 = "Student A"
# elif B_percentage >= A_percentage and B_percentage >= C_percentage:
#     rank1 = "Student B"
# else:
#     rank1 = "Student C"

# # Find lowest
# if A_percentage <= B_percentage and A_percentage <= C_percentage:
#     rank3 = "Student A"
# elif B_percentage <= A_percentage and B_percentage <= C_percentage:
#     rank3 = "Student B"
# else:
#     rank3 = "Student C"


# # Middle rank (whoever is not rank1 and not rank3)
# if rank1 != "Student A" and rank3 != "Student A":
#     rank2 = "StudentA"
# elif rank1 != "Student B" and rank3 != "Student B":
#     rank2 = "StudentB"
# else:
#     rank2 = "StudentC"

# # ------------------------------
# # Step 6: BAR GRAPH using "*"
# # ------------------------------

# A_bar = "*" * int(A_percentage // 2)
# B_bar = "*" * int(B_percentage // 2)
# C_bar = "*" * int(C_percentage // 2)

# # ------------------------------
# # Step 7: Display Results
# # ------------------------------

# print("\n----- FINAL REPORT -----")
# print("Student A:", A_percentage, "% | Pass:", A_result, "| Distinction:", A_distinction)
# print("Student B:", B_percentage, "% | Pass:", B_result, "| Distinction:", B_distinction)
# print("Student C:", C_percentage, "% | Pass:", C_result, "| Distinction:", C_distinction)

# print("\n--- RANKING ---")
# print("Rank 1:", rank1)
# print("Rank 2:", rank2)
# print("Rank 3:", rank3)

# print("\n--- PERFORMANCE BAR GRAPH (Each * = 2%) ---")
# print("A:", A_bar)
# print("B:", B_bar)
# print("C:", C_bar)





# FULL LEVEL 4 CODE

print("----- LEVEL 4: ADVANCED EXAMINATION ANALYZER -----")

# -------------------------------
# Step 1: Input marks
# -------------------------------

print("/n---Student A ---")
a1 = int(input("Maths: "))
a2 = int(input("Science: "))
a3 = int(input("English: "))
a4 = int(input("History: "))
a5 = int(input("Geography: "))

print("/n---Student B ---")
b1 = int(input("Maths: "))
b2 = int(input("Science: "))
b3 = int(input("English: "))
b4 = int(input("History: "))
b5 = int(input("Geography: "))

print("/n---Student C ---")
c1 = int(input("Maths: "))
c2 = int(input("Science: "))
c3 = int(input("English: "))
c4 = int(input("History: "))
c5 = int(input("Geography: "))

# ----------------------------------
# Step 2: Weighted total calculation
# ----------------------------------

# Weightages:
# Maths = ×1.2
# Science = ×1.2
# Others = ×1

A_total = (a1*1.2) + (a2*1.2) + a3 + a4 + a5
B_total = (b1*1.2) + (b2*1.2) + b3 + b4 + b5
C_total = (c1*1.2) + (c2*1.2) + c3 + c4 + c5

A_per = (A_total*100) / 600
B_per = (B_total*100) / 600
C_per = (C_total*100) / 600


# ----------------------------------
# Step 3: Normalization (+5% for all)
# ----------------------------------

A_per = A_per + (A_per * 0.05)
B_per = B_per + (B_per * 0.05)
C_per = C_per + (C_per * 0.05)

# ----------------------------------
# Step 4: Pass/Fail check
# ----------------------------------

def pass_fail(m1, m2, m3, m4 ,m5):
    if m1<m3 or m2<33 or m3<33 or m4<33 or m5<33:
        return "FAIL"
    return "PASS"

A_res = pass_fail(a1, a2, a3, a4, a5)
B_res = pass_fail(b1, b2, b3, b4, b5)
C_res = pass_fail(c1, c2, c3, c4, c5)



# ----------------------------------
# Step 5: Distinction
# ----------------------------------

def dist(x, result):
    if x >= 75 and result == "pass":
        return"YES"
    return "NO"

A_dist = dist(A_per, A_res)
B_dist = dist(B_per, B_res)
C_dist = dist(C_per, C_res)

# ----------------------------------
# Step 6: Subject-wise Toppers
# ----------------------------------

# Maths
if a1>=b1 and a1>=c1: math_top="A"
elif b1>=a1 and b1>=c1: math_top="B"
else: math_top = "C"

# Science
if a2>=b2 and a2>=c2: science_top="A"
elif b2>=a2 and b2>=c2: science_top="B"
else: science_top = "C"

# English
if a3>=b3 and a3>=c3: Engilsh_top = "A"
elif b3>=a3 and b3>=c3: Engilsh_top = "B"
else: Engilsh_top = "C"

# History
if a4>=b4 and a4>=c4: History_top = "A"
elif b4>=a4 and b4>=c4: History_top = "B"
else: History_top = "C"

# Geography
if a5>=b5 and a5>=c5: Geography_top = "A"
elif b5>=a5 and b5>=c5: Geography_top = "B"
else: Geography_top = "C"

# ----------------------------------
# Step 7: Strongest & Weakest Subject (Student-wise)
# ----------------------------------

def strongest_weakest(m1, m2, m3, m4 ,m5):
    # strongest
    if m1>=m2 and m1>=m3 and m1>=m4 and m1>=m5: strong = "MATHS"
    elif m2>=m1 and m2>=m3 and m2>=m4 and m2>=m5: strong="Science"
    elif m3>=m1 and m3>=m2 and m3>=m4 and m3>=m5: strong="English"
    elif m4>=m1 and m4>=m2 and m4>=m3 and m4>=m5: strong="History"
    else: strong="Geography"

    # weakest
    if m1<=m2 and m1<=m3 and m1<=m4 and m1<=m5: weak="Maths"
    elif m2<=m1 and m2<=m3 and m2<=m4 and m2<=m5: weak="Science"
    elif m3<=m1 and m3<=m2 and m3<=m4 and m3<=m5: weak="English"
    elif m4<=m1 and m4<=m2 and m4<=m3 and m4<=m5: weak="History"
    else: weak="Geography"

    return strong, weak

A_strong, A_weak = strongest_weakest(a1,a2,a3,a4,a5)
B_strong, B_weak = strongest_weakest(b1,b2,b3,b4,b5)
C_strong, C_weak = strongest_weakest(c1,c2,c3,c4,c5)

# ----------------------------------
# Step 8: Ranking + Tie-breaking
# ----------------------------------

if A_per>=B_per and A_per>=C_per:
    R1 = "A"
elif B_per>=A_per and B_per>=C_per:
    R1 = "B"
else:
    R1 = "C"

if A_per<=B_per and A_per<=C_per:
    R3 = "A"
elif B_per<=A_per and B_per<=C_per:
    R3 = "B"
else:
    R3 = "C"

if R1!="A" and R3!="B": R2="A"
elif R1!="B" and R3!="B": R2="B"
else: R2="C"

# TIE BREAKER: If percentages tie → Science marks higher wins

if A_per==B_per:
    if a2>b2: R1="A"
    else: R1="B"

if A_per==C_per:
    if a2>c2: R1="A"
    else: R1="C"

if B_per==C_per:
    if b2>c2: R1="B"
    else: R1="C"


# ----------------------------------
# Step 9: Bar Graph with * and #
# ----------------------------------

def graph(x, dist):
    stars = "*" * int(x//2)
    if dist=="YES":
        stars = stars + "#"
    return stars

A_graph = graph(A_per, A_dist)
B_graph = graph(B_per, B_dist)
C_graph = graph(C_per, C_dist)


# ----------------------------------
# Step 10: Final Output
# ----------------------------------

print("\n----- FINAL REPORT -----")
print("A:", A_per, "% | Pass:", A_res, "| Distinction:", A_dist, "| Strong:", A_strong, "| Weak:", A_weak)
print("B:", B_per, "% | Pass:", B_res, "| Distinction:", B_dist, "| Strong:", B_strong, "| Weak:", B_weak)
print("C:", C_per, "% | Pass:", C_res, "| Distinction:", C_dist, "| Strong:", C_strong, "| Weak:", C_weak)

print("\n--- SUBJECT TOPPERS ---")
print("Maths:", math_top)
print("Science:", science_top)
print("English:", Engilsh_top)
print("History:", History_top)
print("Geography:", Geography_top)

print("\n--- RANKING ---")
print("Rank 1:", R1)
print("Rank 2:", R2)
print("Rank 3:", R3)

print("\n--- PERFORMANCE GRAPH ---")
print("A:", A_graph)
print("B:", B_graph)
print("C:", C_graph)