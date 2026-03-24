# Write a program to conduct a multiple choice quiz 
# and calculate the score of the user
q1 = """
Read and choose the correct option
Q1: One of the folloiwng is the importance of balance diet
A. Good health
B. Disease
C. Fighting
"""

q2 = """
Read and choose the correct option
Q2: Food is important for man's survival
A. True
B. Not Important
C. False
"""

q3 = """
Read and choose the correct option
Q3: We eat because we want to fight people
A. Yes
B. Possible
C. No
"""


def multiplechoice():
    a = input(q1 + " Input the correct option: ").upper()
    b = input(q2 + " Input the correct option: ").upper()
    c = input(q3 + " Input the correct option: ").upper()
    
    score = 0
    
    # Check the answers
    if a == "A":
        score += 1
    
    if b == "A":
        score += 1
    
    if c == "C":
        score += 1
    else:
        return ("Incorrect Option")
    
    percentage = round((score / 3) * 100, 2)
    return score, percentage
gr = input("Your Name: ")
hr = input("Your Student Number: ")      
score, percentage = multiplechoice()
print(f"{gr} with student number {hr} your score is: {percentage} %")