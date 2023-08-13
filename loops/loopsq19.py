# Write a Python function to check if a list contains any negative numbers using a for loop and if-els:
list =[23,34,-56,67,-98,43]
positive =0
negative=0
for i in list:
    if (i>0):
        positive=positive+1
    else:
        negative = negative+1
        print("positive number in list", positive)
        print("negative number in list", negative)