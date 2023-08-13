# Write a Python function that removes all duplicates from a list using a for loop and if-else.
user_input=[20,10,20,30,40,50,60,50,70,60]
result=[]
for i in user_input:
    if i not in result:
       result.append(i)
    print(result)
