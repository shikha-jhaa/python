# Write a Python function to check if two lists have at least one common element using a for loop and if-else.
list1=[2,3,4,5,6,7]
list2=[9,10,11,12,13,5,6,7]
result=False
for a in list1:
    for b in list2:
        if (a==b):
            result=True
            if result==True:
             print("lists have common elements")
    else:
        print("lists do not have common elements")