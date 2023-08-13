user_input=int(input("enter the year:"))
if user_input%400==0: 
    print(user_input,"is a leap year")
elif (user_input%4==0 and user_input%100!=0):
    print(user_input,"is a leap year")
else:
    print(user_input,"is not a leap year")




