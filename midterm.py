# Name: Ravish Kamath
# Student ID: 213893664
# Email: ravish96@my.yorku.ca
# Section B

def task0():
    print("Midterm Exam - EECS1015")
    print("Name: Your Name")
    print("Student ID: 213893664")
    print("email: ravish96@my.yorku.ca")
    print("Section B")


def task1():
    fName = input("Your first name: ")
    fName = fName.strip().capitalize()
    lName = input("Your last name: ")
    lName = lName.strip().upper()
    init = float(input("Initial funds to invest: $ "))
    perc = float(input("Annual return percentage: "))
    print(f"Yearly return for {fName} {lName}")
    print(f"Initial deposit: {init}")

    for i in range(1,6):
        i = i
        init = init + (init * (perc/100))
        print(f"Year {i}: {init:.2f}")


def task2():
    print("Soda Vending Machine")

    amount = 0.00

    while amount < 1.00:
        print(f"Current amount ${amount:.2} out of $1.00")
        print("Insert Coin")
        print("1. Toonie  ($2.00)")
        print("2. Loonie  ($1.00)")
        print("3. Quarter ($0.25)")
        print("4. Dime    ($0.10)")
        print("5. Nickel  ($0.05)")
        x = int(input("Selection [1-5]? "))
        if x < 1 or x > 5:
            print("Invalid Selection!")
        elif x == 1:
            amount = amount + float(2.00)
        elif x == 2:
            amount = amount + float(1.00)
        elif x == 3:
            amount = amount + float(0.25)
        elif x == 4:
            amount = amount + float(0.10)
        elif x == 5:
            amount = amount + float(0.05)
        if amount < 1.00:
            pass

    rem = amount - 1
    print(f"Total amount provided: ${amount:.2}")

    if rem > 0:
        print("Thank you for your purchase")
        print(f"Please take your change {rem:.2}")
    else:
        print("Thank you for your purchase")

def task3():
    from random import randint
    print(" ")
    prompt = "Y"
    while prompt == "Y":
        print("Dice Game")
        print("Rolling Die 10 times")
        sum = 0
        counter = 0
        for i in range(1,11):
            x = randint(1,6)
            print(f"Roll {i}: [{x}]")
            sum = sum + x
            if x == 1:
                counter = counter + 1
        prompt = "null"
        if counter == 2:
            print("+10 Bonus for snake eyes [1][1]!")
            sum = sum + 10
        if sum > 35:
            print(f"Total {sum} -- OVER 35 POINTS [YOU WIN!]")
        else:
            print(f"Total {sum} -- TOO FEW POINTS [YOU LOSE!]")
        prompt = input("Enter 'Y' to play again: ")
        prompt = prompt.upper()

def task4():
    global string
    def countCases(string):
        global count_Upper
        global count_Lower
        count_Upper = 0
        count_Lower = 0
        for i in string:
            if i.isupper():
                count_Upper = count_Upper + 1
            elif i.islower():
                count_Lower = count_Lower + 1
            else:
                pass

        return count_Upper, count_Lower

    def flipCase(string):
        global letter
        letter = ""
        for i in string:
            if i.isupper():
                letter = letter + i.lower()
            elif i.islower():
                letter = letter + i.upper()
            else:
                letter = letter + i
        return letter
    def cutQuotedText(string):
        word = string
        start_cut = word.find('"')
        end_cut = word.find('"', start_cut + 1 )
        quote = string[start_cut: end_cut + 1]
        word = string.replace(quote, " ")
        return word


    string = input("Enter string with one with \"quotes\": ")
    string_Upper, string_Lower = countCases(string)
    flip = flipCase(string)
    print(f"This string has {string_Upper} uppercase characters.\nThis string has {string_Lower} lower characters.")
    print(f"Case flip: \'{flip}\'")
    if string.count("\"") == 2:
        quote_R = cutQuotedText(string)
        print(f"Quote removed: '{quote_R}'")
    else:
        print("Quote removed: 'ERROR! No quoted text.'")

def main():
    print("\n")
    task0()
    print("\n----------Task 1-----------")
    task1()
    print("\n----------Task 2-----------")
    task2()
    print("\n----------Task 3-----------")
    task3()
    print("\n----------Task 4-----------")
    task4()
    input("\nPress enter to exit.")

if __name__ == '__main__':
    main()