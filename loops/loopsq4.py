# create a python program to check number is prime or not using a for loops and if_else statements:
user_input=int(input("enter the number:"))
# boolean condition
flag=True
for i in range (2, user_input):
 if user_input%i==0:
    flag=False
if flag==True:
    print(user_input,"is a prime number")
else:
    print(user_input,"is not a prime number")
