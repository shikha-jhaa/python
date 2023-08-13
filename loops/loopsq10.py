# Create a program that prints a pattern of stars in a right-angled triangle using a for loop.
noofRows= int(input("enter the number of rows:"))

for rowsNo in range(1,noofRows+1):
    
    print("*  "* rowsNo)
