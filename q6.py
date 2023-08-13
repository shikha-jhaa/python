# check a program if a year is century or not:
user_input=int(input("enter the year"))
if user_input<=0:
     print('year is 0')
elif user_input%100==0:
    print("user_input // 100, century")
elif user_input<=0:
    print("1st century")
else:
     print(user_input // 100+1,"century")    
        