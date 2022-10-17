# Lab 3
# Author: Ravish Kamath
# Email: ravish96@my.yorku.ca
# Student ID: 213893664
# Section B

#Task 1
print("--- Task 1 ---: Compute Fare")
print("(1) One way or (2) round trip?")
trip = int(input("Enter 1 or 2: "))
print("Select Age Range:")
print("(1) Under 12\n(2) 13-64\n(3) 65 or older")
age = int(input("Enter 1, 2, or 3: "))

if trip == 1:
    if (age == 1) or (age == 3):
        print("Total amount due: $0.90 [one way (reduced fare)]")
    else:
        print("Total amount due: $1.80 [one way (full fare)]")
else:
    if (age == 1) or (age == 3):
        print("Total amount due: $1.75 [round trip (reduced fare)]")
    else:
        print("Total amount due: $3.50 [round trip (full fare)]")

# Task 2
print("--- Task 2 ---: Parse string")
z = input("Input a string: ")
t = ""
for i in range(0, len(z),1):
    if z[i] in [" "]:
        print(f"str[{i}] = SPACE")
    else:
        print(f"str[{i}] = {z[i]}")

for j in range(len(z)-1, -1, -1):
    if z[j] == " ":
        t = t
    else:
     t = t + z[j]


print(f"Reverse no spaces: {t}")

#Task 3
print("--- Task 3 ---: The maximum *even* number")
print("Keep entering positive integer\nTo quit, input a negative integer")

num = int(input("Enter a number: "))
max_num = 0

while num >= 0:
    num = int(input("Enter a number: "))
    if num <= 0:
        break
    if num % 2 == 0:
        if num > max_num:
            max_num = num

print(f"Largest even number: {max_num}")

#Task 4
print("--- Task 4 ---: Better triangle draw")
n = int(input("Enter size between 5 and 20: "))

while n < 5 or n > 20:
    n = int(input("Enter size between 5 and 20: "))

for i in range(0, n+1):
    output = "\\"
    if i == n:
        output = "|"
    for j in range(0, i):
        output = "-" + output
    print(output)
for k in range(n-1, -1, -1):
    output2 = "/"
    for l in range (k,0,-1):
        output2 = "-" + output2
    print(output2)

input("Press enter to end. . .")

