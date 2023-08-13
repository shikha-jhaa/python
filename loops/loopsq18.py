# Create a program that generates a multiplication table up to a given number using nested for loops.
user_input=int(input("enter the table:"))
i=1
while (i<11):
    print(user_input,"*",i,"=",user_input*i)
    i=i+1 