n = 10
while n >= 0:
    print(n)
    n -= 1

print("Blast off!")

for i in range(3):
    for j in range(4):
        print(i,j)

#USE  A FOR LOOP TO ADD THE NUMBERS FROM 1 TO N(N IS ENTERED BY THE USER)
N = int(input("Enter a number: "))
total = 0
for i in range(1,N+1):
    total = total + i
print(total)
    
