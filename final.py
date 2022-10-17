###########################################
# EECS1015 - Final exam (final.py)
# Name: Ravish Kamath
# Student ID: 213893664
# Email: ravish96@my.yorku.ca
# Section B
###########################################

from random import randint
from utilities import students, studentsInfo
from utilities import SeaLife
import time

def task0():
    print("Midterm Exam - EECS1015")
    print("Name: Your Name")
    print("Student ID: 213893664")
    print("email: ravish96@my.yorku.ca")
    print("Section B")


def task1():
    def printOutcome(userSelection, computerSelection):
        rocPapSisDict = {1: "rock", 2: "paper", 3: "scissors"}
        user = rocPapSisDict[userSelection]
        comp = rocPapSisDict[computerSelection]
        print(f"You: {rocPapSisDict[userSelection]} \nHAL: {rocPapSisDict[computerSelection]}")
        if user == comp:
            print("A tie!")
        elif user == "rock":
            if comp == "scissors":
                print("You win!")
            else:
                print("HAL wins!")
        elif user == "paper":
            if comp == "rock":
                print("You win!")
            else:
                print("HAL wins!")
        elif user == "scissors":
            if comp == "paper":
                print("You win!")
            else:
                print("HAL wins!")

    print("Rock, Paper, Scissors!")
    keepPlay = "Y"
    while keepPlay == "Y":
        userSelect = int(input("Make your selection . . .\n(1) rock, (2) paper, (3) scissors? "))
        while userSelect > 3 or userSelect < 0:
            print("Invalid selection. Try again.")
            userSelect = int(input("Make your selection . . .\n(1) rock, (2) paper, (3) scissors? "))
        halSelect = randint(1, 3)
        printOutcome(userSelect, halSelect)
        keepPlay = input("Play again (Y)? ").strip().upper()


def task2():
    def swapAdjacentElements(alist):
        global lastItem
        assert len(alist) >= 2, "Must enter two or more characters!"
        print(alist)
        print("Modified list")
        n = len(alist)
        if len(alist) % 2 != 0:
            lastItem = alist[-1]
        for i in range(0, len(alist)-1, 2):
            x = i
            y = i + 1
            temp = x
            x = y
            y = temp
            x1, y1 = (alist[x]), (alist[y])
            alist.append(x1)
            alist.append(y1)
        if len(alist) %2 != 0:
            alist.append(lastItem)
        del alist[0:n]
        print(alist)

    alist = input("Input two or more chars separated by spaces: ").split(" ")
    swapAdjacentElements(alist)
    str = ""
    for items in alist:
        str += items
    print(f"string version:'{str.strip()}'")


def task3():
    students.sort()
    for key in studentsInfo:
        studentsInfo[key].sort()
    result = ""
    list = []
    for i in range(0, len(students)):
        x = ("%10s" % students[i])
        result += x + " ("
        for keys, values in studentsInfo.items():
            for j in values:
                if i == j:
                    list.append(keys)
        for l in range(0, len(list)):
            if l == 0:
                result += list[l] + ") Program: "
            elif l == 1:
                result += list[l] + " Housing: "
            elif l == 2:
                result += list[l]
        result += "\n"
        list.clear()
    print(result)

def task4():
    input("Press enter to start aquarium. . . ")
    obj1 = SeaLife(randint(0,1), randint(5,30))
    obj2 = SeaLife(randint(0, 1), randint(5, 30))
    obj3 = SeaLife(randint(0, 1), randint(5, 30))
    obj4 = SeaLife(randint(0,1), randint(5,30))
    obj5 = SeaLife(randint(0, 1), randint(5, 30))
    time1 = 0
    for i in range(0, 50):
        time1 += 1
        print(f"----------------------------------------Time: {time1}")
        print(obj1.getStr())
        print(obj2.getStr())
        print(obj3.getStr())
        print(obj4.getStr())
        print(obj5.getStr())
        obj1.move()
        obj2.move()
        obj3.move()
        obj4.move()
        obj5.move()
        time.sleep(0.3)



def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()
    input("Press enter to quit.")


if __name__ == "__main__":
    main()

