# # print("hello world")
# user_input=int(input("enter the year:"))
# if user_input%400==0:
#     print(user_input,"is a leap year")
# elif (user_input%4==0 and user_input%100!=0):
#     print(user_input,"is a leap year")
# else:
#     print(user_input,"is not a leap year")      
# global_var = 20

# def another_function():
#     print(global_var)

# another_function()
# # The global_var variable can be accessed within the another_function() scope.
# another_function()
# another_function()
# another_function()
# local_var = 10
# fuction 
lv=10
name1="none"
gv=int(input("enter the number:"))
def example_function() :
    Total = (gv+lv)
    global name, name1
    name="shikha"
    print("name 27",name)
    name1="sona"
    print(Total)
example_function()
print("lv31",lv)
print("gv32",gv)
print("name133",name1)
print("name34",name)
                                                                                                       