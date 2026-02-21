# variables
a = 28 # Integer
b = 1.5 #float
c = "Hello!" #string
d = True # bool
e = None #NoneType


# Write a program that accept inputs and be able to say Hello!
name = input("Name: ")
print("Hello," + name)
print(f"Hello, {name}")

# Write a condition 
n: int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

# sequence 
name = "Harry"

print(name[0]) # H
print(name[1]) 

names =  ["Harry", "Ron", "Hermione"]

print(names[0])

coordinate = (10.0, 20.0)

# Define a list of names
names = ["Harry", "Ron", "Hermione", "Ginny"]
print(names[0])

# Add a new item to the list
names.append("Draco")

# Sorting a list
names.sort()

print(names) # "Draco", "Ginny", "Harry", "Hermione",  "Ron"
# create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s) # 1,2,3,4
s.remove(2)
print(s) # 1,3,4

print(f"The set has {len(s)} of elements.")

# Loop
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

names =  ["Harry", "Ron", "Hermione"]

for name in names:
    print(name)

name = "Harry"

for character in name:
    print(character)

houses = {"Harry":"Gryffindor", "Draco":"Slytherin"}

#Add a new item in the dictionary
houses["Hermione"] = "Gryffindor"

print(houses["Harry"])

# Functions
def square(x):
    return x * x

for i in range(10):
    print(f"The sqaure of {i} is {square(i)}")

# Object Oriented Programming
class Point():
    def __init__ (self, x):
        self 




