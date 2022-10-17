# Lab 5
# Author: Ravish Kamath
# Email: ravish96@my.yorku.ca
# Section B
# Student ID: 213893664

from random import randint
import pyttsx3

def task1():
    def generateRandomList(maxValue, size):
        list = []
        for i in range(maxValue):
            randNum = randint(1, size)
            list.append(randNum)
        print(list)
        return list

    def computeAverage(list):
        num = 0
        for i in list:
            addNum = num + i
            num = addNum
        avg = addNum/ len(list)
        return avg

    prompt = int(input("Input list size: "))
    prompt_2 = int(input("Input max int: "))
    randList = generateRandomList(prompt, prompt_2)
    avg_randList = computeAverage(randList)
    print(f"Average value = {avg_randList:.4f} ")

def task2():
    def stringToCharLst(inputString):
        numList = []
        for i in inputString:
            numList.append(i)
        return numList

    def charsToWord(listA):
        numDict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven", "8": "eight",
                   "9": "nine", "-": "dash"}
        letterList = []
        for items in listA:
            word =(numDict[items])
            letterList.append(word)
        seperator = "->"
        sepList = seperator.join(letterList)
        return letterList, sepList

    def foo():
        engine = pyttsx3.init()
        for items in wordNum_1:
            engine.say(items)
        engine.runAndWait()

    print("Enter phone number as XXX-XXX-XXXX")
    prompt = (input("Type here: "))
    listNum = stringToCharLst(prompt)
    print(listNum)
    wordNum_1 , wordNum_2  = charsToWord(listNum)
    print(wordNum_1)
    print(wordNum_2)
    prompt2 = input("Say word list? (Y/N) ")
    prompt3 = prompt2.upper()
    if prompt3 == "Y":
        foo()

def main():
    print("\n--------- TASK 1: Random List -------------")
    task1()
    print("\n--------- TASK 2: Phone number to text ---")
    task2()
    input("Press enter to exit.")


if __name__ == "__main__":
    main()
