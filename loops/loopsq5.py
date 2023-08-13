# create a program to count vowels of a given strings using a for loop and if_else statements :
str1=input("enter the string:")
print(str1)
count=0
vowels = ["a","e","i","o","u"]
for character in str1:
 if character in vowels:
    count=count+1
    print("number of vowels in given sentence:",count)
