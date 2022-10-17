# Lab 2
# Author: Ravish Kamath
# Email: ravish96@my.yorku.ca
# Student ID: 213893664
# Section B
#Task 1
##

print("---Task 1---- BMI Calculator")
#input data
name = input("Name: ")
weight_kg = input("Weight (kg):")
height_cm = input("Height (cm):")

#process name
name = name.strip()
name = name.title()

#proess weight
weight_kg = float(weight_kg)

#process height
height_m = float(height_cm)/100

# BMI
BMI = float((weight_kg)/((height_m)**2))


print ( "Name: {} Weight: {:.2f} Height [meters]: {:.2f} BMI: {:.2f}" .format(name, weight_kg, height_m, BMI))





#Task 2
##

print("---Task 2---- Leetspeak Converter")
# input data
text = input( "Type a long string: ")

#process string
text = text.strip().upper()
text = text.replace("T", "+").replace("A", "@").replace("E", "3").replace("I", "|").replace("B", "8").replace("O", "0")
text = text.replace("C", "[").replace("S", "5")
print(text)




#Task 3

print("---Task 3---- Flipping String")
text1 = input("Input a long string: ")

strng_len = len(text1)
midCharInt = (len(text1)//2)
midChar = text1[midCharInt]

print("This string is {} characters long. The middle character is '{}'" .format(strng_len,midChar))
print("Flipped String")

text1 = text1.upper()
seperatorIndex = text1.find(text1[midCharInt], midCharInt-1)
begChar = text1[0:seperatorIndex]
endChar = text1[seperatorIndex:]

flipString = endChar + "|" + begChar


print(flipString)

#Task4

print("---Task 4---- Multiple numbers")

numbersStrng = input("Input numbers to multiply: ")

numbersStrng = numbersStrng.strip()
numbersStrng = "" .join(numbersStrng.split())


seperatorIndex_1 = numbersStrng.find("*")
number1 = (numbersStrng[0:seperatorIndex_1])
number2 = (numbersStrng[seperatorIndex_1+1:])

print("Extracted numbers {} {}" .format(number1, number2))

result = int(number1)*int(number2)
print ("{} * {} = {}" .format(number1,number2,result))
print(numbersStrng)

input("Press enter to end. . .")












