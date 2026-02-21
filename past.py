name= "pius"
age= "21"



def callname():
    name= "wisdom"
    age= "20"
    return("My name is "+ name + " and I am " + age + " years old")
    
print(callname())

def guidecall():
    name = input("Name: ")
    age = int(input("Age: "))

    if age < 18:
        return(f"{name} please stay away from achohol")
    else:
       return(f"{name} please drink responsibly")

print(guidecall())

# Function to calculate the area of a house in sqm
def area():
    l = int(input("length in sqm: "))
    b = int(input("breadth in sqm: "))
    a = l * b
    return(f"The area of the house is {a} sqm")

print(area())
