# Lab 8
# Author: Ravish Kamath
# Email: ravish96@my.yorku.ca
# Student ID: 213893664
# Section B

from random import randint
import time

class Snail:
    snails = ["__~@", "_~_@", "~__@"]

    def __init__(self, name =""):
        assert len(name) <= 2, "Snail's initials must be 2 characters"
        self.name = name.upper()
        self.speed = float((randint(1, 10))/10)
        self.frame = 0
        self.pos = 0.0

    def move(self):
        self.pos = self.pos + self.speed
        if self.frame <= 2:
            self.frame += 1
        else:
            self.frame = self.frame
        if self.frame >= 3:
            self.frame = 0

    def getIntPos(self):
        return int(self.pos)

    def getName(self):
        return self.name

    def getStr(self):
        self.result = ""
        for num in range(0, int(self.pos)):
            self.result = self.result + " "
        self.result = self.result + Snail.snails[self.frame]
        for num in range(0, 40 - int(self.pos)):
            self.result += " "
        self.result = self.result + " " + self.name

        return self.result

    def getSnailList(self):
        self.snailList = Snail()
        self.snailList = []
        n = int(input("How many snails are racing? "))
        for i in range(n):
            self.initials = input(f"Snail {i+1} two initials: ")
            self.snailList.append(Snail(self.initials))
        return self.snailList


    def runRace(self, snailList):
        input("Press enter to start race. ")
        timeStep = 1
        while int(self.pos) < 40:
            print(f"----------------------------------------Time {timeStep} ")
            timeStep += 1
            for i in range(0,len(snailList)):
                snailList[i].getStr()
                print(snailList[i].getStr())
                snailList[i].move()
                y = snailList[i].getIntPos()
                time.sleep(0.2)
                if y > 39:
                    winner = snailList[i]
                    break

        print("Snail " + winner.name + " WON!")


def main():
    x = "Y"
    while x == "Y":
        print("Snail Race . . . .")
        w = Snail()
        z  = w.getSnailList()
        w.runRace(z)
        x = str(input("Play again (Y)? "))
    print("DONE.  Type Enter to exit.")
    input()


if __name__ == "__main__":
    main()
