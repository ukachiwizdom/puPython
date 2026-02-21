


# Write a program 
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
c. False
"""

q3 = """
Read and choose the correct option
Q3: We eat because we want to fight people
A. Yes
B. Possible
c. No
"""

def multiplechoice():
    a = (input(q1 + " Input the correct option: ")).upper()
    b = input(q2 + " Input the correct option: ").upper()
    c = input(q3 + " Input the correct option: ").upper()
    
    # Check the answers
    if a == "A":
        return("Correct Answer")
    else:
        return("Incorrect Answer")  
    
    if b == "A":
        return("Correct Answer")
    else:
        return("Incorrect Answer")  
   
    if c == "C":
        return("Correct Answer")
    else:
        return("Incorrect Answer")  
  
 r = "Correct Answer":
         
print(multiplechoice())

def percentage():
for r in ({a}, {b}, {c}):
    return(r / 3 * 100)


print("Your score is:", percentage)