# Sum project 
# Sum 10 digits untered as input by the user
i = 0
s = 0

while i < 10:
    n = int(input("Enter Number: ")) 
    s += n # add the number each time
    i += 1  

print("The sum of the numbers is: ",s)


# The for loop  solution

total = 0

for i in range(10):
    n = int(input("Number: "))
    total = total + n

print("Sum is: ", total)
