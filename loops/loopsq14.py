string="abcdaaabbccddeefghij"
character=input("enter the character:")
i=0
count=0
while (i<len(string)):
       if (string[i]==character):
            count=count+1
            i += 1
            print("Total number of", character,"is",count)