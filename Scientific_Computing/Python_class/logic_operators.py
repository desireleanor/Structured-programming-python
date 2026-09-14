#and 
#or
print(True and True)   #True
print(True and False)  #False
print(False and True)  #False
print(False and False) #False

print(True or True)    #True
print(True or False)   #True
print(False or True)   #True
print(False or False)  #False

test1 = int(input("Enter the score of the first test: "))
test2 = int(input("Enter the score of the second test: "))
test3 = int(input("Enter the score of the third test: "))

avg = (test1 + test2 + test3)/3
print("Your average score is: ", avg)

if avg >= 90:
    print("Congratulations on a High Average!")




